"""
Вася просил Аллу помочь решить задачу. На этот раз по информатике.

Для неотрицательного целого числа X списочная форма –— это массив его цифр слева направо. К примеру, для 1231 списочная форма будет [1,2,3,1].
На вход подается количество цифр числа Х, списочная форма неотрицательного числа Х и неотрицательное число K. Число К не превосходят 10000. Длина числа Х не превосходит 1000.

Нужно вернуть списочную форму числа X + K.

Не используйте встроенные средства языка для сложения длинных чисел.

Формат ввода
В первой строке — длина списочной формы числа X. На следующей строке — сама списочная форма с цифрами записанными через пробел.

В последней строке записано число K, 0 ≤ K ≤ 10000.

Input:
4
1 2 0 0
34


Output:
1 2 3 4
"""


def sum_bitwise(a: list, b: list) -> list:
    extra = 0
    result = []
    for i in range(max(len(a), len(b))):
        operand_1 = int(a[-i - 1]) if abs(-i - 1) <= len(a) else 0
        operand_2 = int(b[-i - 1]) if abs(-i - 1) <= len(b) else 0

        local_sum = operand_1 + operand_2 + extra
        result.append(local_sum % 10)
        extra = local_sum // 10

    while extra > 0:
        result.append(extra % 10)
        extra = extra // 10

    return result[::-1]


if __name__ == '__main__':
    n = int(input())
    a = list(map(int, input().split()))
    b = list(map(int, list(input())))

    result = sum_bitwise(a, b)
    print(' '.join(map(str, result)))
