# https://contest.yandex.ru/contest/22779/run-report/112428311/
#
# Рекурсивная функция для расчета чисел Фибоначчи.
# Используется мемоизация для сохранения промежуточных результатов вычисления. Таким образом, каждое значение функции _fibonacci() вычисляется только один раз.
# Это требует дополнительной памяти, пропорционально величине n.
#
# Временная сложность - O(N). Расчет каждого из n значений производится только один раз. Последующий вызов функции с сохраненными значениями выполняется за O(1) и не делает дополнительных рекурсивных вызовов.
# Сложность по памяти - O(N). Состоит из размера словаря O(n) и размера стека вызовов O(n)

def fibonacci(n: int) -> int:
    values = {
        0: 1,
        1: 1
    }
    return _fibonacci(n, values)


def _fibonacci(n: int, values: dict) -> int:
    if n in values:
        return values[n]

    value = _fibonacci(n - 1, values) + _fibonacci(n - 2, values)
    values[n] = value

    return value


def main():
    n = int(input())
    print(fibonacci(n))


if __name__ == '__main__':
    main()
