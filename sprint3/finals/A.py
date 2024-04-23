"""
https://contest.yandex.ru/contest/23815/run-report/113539254/

Алгоритм предназначен для поиска элемента target в отсортированном массиве, который был "сломан" (т.е. изначально данные хранились в кольцевом буфере и при копировании произошло смещение).
После смещения массив можно представить как состоящий из двух отсортированных частей, разделенных границей.

Идея алгоритма заключается в использовании модифицированной версии бинарного поиска.
Вначале алгоритм проверяет, сломан ли массив (т.к. смещение может быть равно 0 и массив будет полностью отсортирован).
Если массив сломан, то алгоритм выбирает разделяющий элемент (sep), который будет первым элементом в левом отсортированном подмассиве (все элементы правого подмассива будут строго меньше sep, а все элементы левого больше либо равны sep).
Затем алгоритм использует модифицированный бинарный поиск для поиска элемента в массиве.

В модифицированной версии бинарного поиска выбирается центральный элемент и проверяется к какому подмассиву он относится, левому или правому.
Если к правому и искомый элемент больше центрального и меньше sep (nums[mid] < target < sep), то продолжаем в правой части массива, иначе в левой.
Если к левому и искомый элемент больше либо равен sep, но меньше центрального (sep <= target < nums[mid]), то продолжаем в левой части массива, иначе в правой.

Сложность по времени: O(log(N)), где N - длина массива; так как каждый шаг алгоритма сужает область поиска вдвое.
Сложность по памяти: O(1), используется константное количество памяти за счет ухода от использования рекурсии
"""


def broken_search(nums: list, target: int) -> int:
    return binary_search_separated(nums, target, 0, len(nums) - 1, nums[0])


def binary_search_separated(nums: list, target: int, idx_l: int, idx_r: int, sep: int) -> int:
    while idx_l <= idx_r:
        mid = (idx_l + idx_r) // 2

        if nums[mid] == target:
            return mid

        if nums[mid] < sep:
            # right sorted array
            if nums[mid] < target < sep:
                idx_l = mid + 1
            else:
                idx_r = mid - 1
        else:
            # left sorted array
            if sep <= target < nums[mid]:
                idx_r = mid - 1
            else:
                idx_l = mid + 1

    return -1


def test():
    arr = [19, 21, 100, 101, 1, 4, 5, 7, 12]
    assert broken_search(arr, 5) == 6
    assert broken_search(arr, 21) == 1
    assert broken_search(arr, 100) == 2
    assert broken_search(arr, 12) == 8

    arr = [99, 111, 120, 131, 1, 4, 5, 7, 12, 64, 77, 86, 98]

    assert broken_search(arr, 7) == 7
    assert broken_search(arr, 131) == 3
    assert broken_search(arr, 86) == 11
    assert broken_search(arr, 64) == 9
    assert broken_search(arr, 111) == 1
    assert broken_search(arr, 98) == 12
    assert broken_search(arr, 112) == -1
    assert broken_search(arr, 99) == 0

    arr = [1, 4, 5, 7, 12, 64, 77, 86, 98, 99, 111, 120, 131]

    assert broken_search(arr, 7) == 3
    assert broken_search(arr, 131) == 12
    assert broken_search(arr, 86) == 7
    assert broken_search(arr, 64) == 5
    assert broken_search(arr, 111) == 10
    assert broken_search(arr, 112) == -1
    assert broken_search(arr, 1) == 0


if __name__ == '__main__':
    test()
