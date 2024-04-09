"""
Представьте себе онлайн-игру для поездки в метро: игрок нажимает на кнопку, и на экране появляются три случайных числа.
Если все три числа оказываются одной чётности, игрок выигрывает.

Напишите программу, которая по трём числам определяет, выиграл игрок или нет.

Input:
1 2 -3
Output:
FAIL
"""


def is_even(val: int) -> bool:
    return val % 2 == 0


def is_win(a: int, b: int, c: int) -> bool:
    expect_even = is_even(a)

    if is_even(b) != expect_even or is_even(c) != expect_even:
        return False

    return True


if __name__ == '__main__':
    a, b, c = map(int, input().split())
    result = is_win(a, b, c)
    print('WIN' if result else 'FAIL')
