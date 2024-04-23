"""
Смержить отрезки.

Формат вывода
Нужно вывести координаты каждой из получившихся клумб в отдельных строках. Данные должны выводиться в отсортированном порядке —– сначала клумбы с меньшими координатами, затем —– с бОльшими.

Input:
4
7 8
7 8
2 3
6 10

Output:
2 3
6 10

"""


def merge_array(values: list[list[int]]) -> list[list[int]]:
    values.sort(key=lambda x: (x[0], x[1]))

    result = [values[0]]
    for i in range(1, len(values)):
        if values[i][0] <= result[-1][1]:
            result[-1][1] = max(values[i][1], result[-1][1])
        else:
            result.append(values[i])

    return result


def main():
    n = int(input())
    values = []
    for i in range(n):
        values.append(list(map(int, input().split())))

    result = merge_array(values)
    print('\n'.join((f'{lf} {rg}' for lf, rg in result)))


if __name__ == '__main__':
    main()
