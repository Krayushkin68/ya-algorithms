"""
Вася реализовал функцию, которая переводит целое число из десятичной системы в двоичную. Но, кажется, она получилась не очень оптимальной.

Попробуйте написать более эффективную программу.

Input:
14
Output:
1110
"""


def convert_to_binary(value: int) -> str:
    if value == 0:
        return '0'

    residual = value
    bits = []
    while residual > 0:
        bits.append(residual % 2)
        residual = residual // 2

    return ''.join(map(str, bits[::-1]))


if __name__ == '__main__':
    value = int(input())
    result = convert_to_binary(value)
    print(result)
