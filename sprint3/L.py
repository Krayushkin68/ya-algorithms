"""
Вася решил накопить денег на два одинаковых велосипеда — себе и сестре. У Васи есть копилка, в которую каждый день он может добавлять деньги (если, конечно, у него есть такая финансовая возможность). В процессе накопления Вася не вынимает деньги из копилки.

У вас есть информация о росте Васиных накоплений — сколько у Васи в копилке было денег в каждый из дней.

Ваша задача — по заданной стоимости велосипеда определить

первый день, в которой Вася смог бы купить один велосипед,
и первый день, в который Вася смог бы купить два велосипеда.
Подсказка: решение должно работать за O(log n).

Формат ввода
В первой строке дано число дней n, по которым велись наблюдения за Васиными накоплениями. 1 ≤ n ≤ 106.

В следующей строке записаны n целых неотрицательных чисел. Числа идут в порядке неубывания. Каждое из чисел не превосходит 106.

В третьей строке записано целое положительное число s — стоимость велосипеда. Это число не превосходит 106.

Формат вывода
Нужно вывести два числа — номера дней по условию задачи.

Если необходимой суммы в копилке не нашлось, нужно вернуть -1 вместо номера дня.


Input:
6
1 2 4 4 6 8
3

Output:
3 5
"""


def search_binary_first(values: list[int], search: int) -> int:
    if search > values[-1]:
        return -1

    return _search_binary_first(values, search, 0, len(values) - 1)


def _search_binary_first(values: list[int], search: int, left_idx: int, right_idx: int) -> int:
    if left_idx > right_idx:
        return -1

    mid = (left_idx + right_idx) // 2

    if values[mid] < search:
        return _search_binary_first(values, search, mid + 1, right_idx)
    elif values[mid] >= search:
        if mid > left_idx and values[mid - 1] >= search:
            return _search_binary_first(values, search, left_idx, mid - 1)
        return mid


def main():
    n = int(input())
    values = list(map(int, input().split()))
    cost = int(input())

    first = search_binary_first(values, cost)
    second = search_binary_first(values, cost * 2)

    first = first + 1 if first != -1 else -1
    second = second + 1 if second != -1 else -1
    print(f'{first} {second}')


if __name__ == '__main__':
    main()
