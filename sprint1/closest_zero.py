"""
Тимофей ищет место, чтобы построить себе дом. Улица, на которой он хочет жить, имеет длину n, то есть состоит из n одинаковых идущих подряд участков. Каждый участок либо пустой, либо на нём уже построен дом.

Общительный Тимофей не хочет жить далеко от других людей на этой улице. Поэтому ему важно для каждого участка знать расстояние до ближайшего пустого участка. Если участок пустой, эта величина будет равна нулю — расстояние до самого себя.

Помогите Тимофею посчитать искомые расстояния. Для этого у вас есть карта улицы. Дома в городе Тимофея нумеровались в том порядке, в котором строились, поэтому их номера на карте никак не упорядочены. Пустые участки обозначены нулями.

Формат ввода
В первой строке дана длина улицы —– n (1 ≤ n ≤ 106). В следующей строке записаны n целых неотрицательных чисел — номера домов и обозначения пустых участков на карте (нули).
Гарантируется, что в последовательности есть хотя бы один ноль. Номера домов (положительные числа) уникальны и не превосходят 109.

Формат вывода
Для каждого из участков выведите расстояние до ближайшего нуля. Числа выводите в одну строку, разделяя их пробелами.

Input:
5
0 1 4 9 0

Output:
0 1 2  0

"""


def get_closest_zeroes(length: int, numbers: list) -> list:
    distances = [-1] * length

    left_zero_idx = None
    right_zero_idx = None

    j = length - 1
    for i in range(length):
        if numbers[i] == 0:
            left_zero_idx = i

        if numbers[j] == 0:
            right_zero_idx = j

        if left_zero_idx is not None:
            left_distance = i - left_zero_idx
            distances[i] = left_distance if distances[i] == -1 else min(left_distance, distances[i])

        if right_zero_idx is not None:
            right_distance = right_zero_idx - j
            distances[j] = right_distance if distances[j] == -1 else min(right_distance, distances[j])

        j -= 1

    return distances


if __name__ == '__main__':
    n = int(input())
    values = list(map(int, input().split()))

    result = get_closest_zeroes(n, values)
    print(' '.join(map(str, result)))
