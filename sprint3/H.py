"""
Формат ввода
В первой строке записано n — количество чисел. Оно не превосходит 100.
Во второй строке через пробел записаны n неотрицательных чисел, каждое из которых не превосходит 1000.

Формат вывода
Нужно вывести самое большое число, которое можно составить из данных чисел.

Input:
3
15 56 2

Output:
56215

Input:
3
269 263 26

Output:
26926326

Input:
3
88 89 8 83 82

Output:
898888382
"""


def sort_key(value: str):
    return value + value[0] * (4 - len(value)), value[-1]


def main():
    n = int(input())
    values = input().split()

    values.sort(key=sort_key, reverse=True)
    print(''.join(values))


if __name__ == '__main__':
    main()
