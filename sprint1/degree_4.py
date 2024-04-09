"""
Напишите программу, которая определяет, будет ли положительное целое число степенью четвёрки.

Подсказка: степенью четвёрки будут все числа вида 4n, где n – целое неотрицательное число.
"""


def is_degree_4(val: int) -> bool:
    while val > 1:
        if val % 4 != 0:
            return False
        val = val // 4

    return True


if __name__ == '__main__':
    val = int(input())
    result = is_degree_4(val)
    print(result)
