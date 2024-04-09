"""
Тимофей записал два числа в двоичной системе счисления и попросил Гошу вывести их сумму, также в двоичной системе.
Встроенную в язык программирования возможность сложения двоичных чисел применять нельзя. Помогите Гоше решить задачу.

Решение должно работать за O(N), где N –— количество разрядов максимального числа на входе.

Input:
1010
1011

Output:
10101
"""


def sum_binary(a: str, b: str) -> str:
    extra = 0
    result = []
    for i in range(max(len(a), len(b))):
        operand_1 = int(a[-i - 1]) if abs(-i - 1) <= len(a) else 0
        operand_2 = int(b[-i - 1]) if abs(-i - 1) <= len(b) else 0

        local_sum = operand_1 + operand_2 + extra
        result.append(local_sum % 2)
        extra = local_sum // 2

    while extra > 0:
        result.append(extra % 2)
        extra = extra // 2

    return ''.join(map(str, result[::-1]))


if __name__ == '__main__':
    a = input()
    b = input()

    result = sum_binary(a, b)
    print(result)
