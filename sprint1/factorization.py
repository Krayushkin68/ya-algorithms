"""
Основная теорема арифметики говорит: любое число раскладывается на произведение простых множителей единственным образом, с точностью до их перестановки. Например:

Число 8 можно представить как 2 × 2 × 2.
Число 50 –— как 2 × 5 × 5 (или 5 × 5 × 2, или 5 × 2 × 5). Три варианта отличаются лишь порядком следования множителей.
Разложение числа на простые множители называется факторизацией числа.

Напишите программу, которая производит факторизацию переданного числа.

Input:
100

Output:
2 2 5 5
"""


def factorize(value: int) -> list[int]:
    divider = 2
    dividers = []
    while divider ** 2 <= value:
        while value % divider == 0:
            value = value // divider
            dividers.append(divider)

        divider += 1

    if value != 1:
        dividers.append(value)

    return dividers


if __name__ == '__main__':
    val = int(input())
    result = factorize(val)

    print(' '.join(map(str, result)))
