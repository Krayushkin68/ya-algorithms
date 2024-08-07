"""
https://contest.yandex.ru/contest/25597/run-report/116344638/

Необходимо определить, можно ли разделить массив на две части так, чтобы сумма элементов в них была одинакова.

Находим общую сумму всех элементов массива. Если она нечетная, то разделить массив на две части невозможно, так как значения целочисленные.
Иначе, необходимо проверить, существует ли подмножество, сумма элементов которого равна половине общей суммы.

Описание алгоритма ДП:
    dp - массив размером равным половине суммы, в i-м элементе хранится информация о том, существует ли подмассив, из которого можно составить сумму i;
    базовый случай - dp[0] = True, так как сумму 0 можно составить из пустого подмножества;
    переход динамики - для каждого элемента value массива values верно, что если существует подмножество, сумма которого равна i - value, то добавив к нему value, мы получим подмножество с суммой i;
                       если dp[i] уже равно True, то изменения не требуются,
                       иначе dp[i] = dp[i] or dp[i - value].

                       Значение i уменьшается от target до value.

    ответом на задачу будет значение dp[-1].

Сложность по памяти O(sum(values) / 2), что равняется длине массива dp.
Сложность по времени O(n * (sum(values) / 2)), так как для каждого элемента массива values мы проходим по всем значениям в dp.
"""


def main():
    n = int(input())
    values = list(map(int, input().split()))

    total = sum(values)
    if total % 2 != 0:
        print('False')
        return

    target = total // 2

    dp = [False] * (target + 1)
    dp[0] = True

    for value in values:
        for i in range(target, value - 1, -1):
            dp[i] = dp[i] or dp[i - value]

    print('True' if dp[-1] else 'False')


if __name__ == '__main__':
    main()
