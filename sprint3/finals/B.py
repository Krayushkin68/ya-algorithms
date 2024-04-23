"""
https://contest.yandex.ru/contest/23815/run-report/113540347/

Алгоритм реализует быструю сортировку in-place с использованием компаратора для сравнения элементов.

В контексте задачи мы сравниваем тройки значений (логин, число решенных задач, штраф).
Функция-компаратор задает параметры сравнения двух наборов.

Сложность по времени: O(n*log(n)) (в худшем случае O(n^2)), стандартная сложность быстрой сортировки, опорный элемент выбирается случайно для уменьшения вероятности работы за O(n^2)
Сложность по памяти: O(log(n)) (в худшем случае O(n)), память расходуется на рекурсивные вызовы

Примечание. Компаратор оставил, т.к. им проще настраивать порядок сортировки,
            но и класс результата добавил чтобы понятнее задать операции сравнения для объектов
"""
import functools
import random
from dataclasses import dataclass
from typing import Callable


def quick_sort(arr: list, cmp: Callable) -> None:
    return _quick_sort(arr, cmp, 0, len(arr) - 1)


def _quick_sort(arr: list, cmp: Callable, idx_l: int, idx_r: int) -> None:
    if idx_l >= idx_r:
        return

    pivot_idx = _partition(arr, cmp, idx_l, idx_r)

    _quick_sort(arr, cmp, idx_l, pivot_idx - 1)
    _quick_sort(arr, cmp, pivot_idx, idx_r)


def _partition(arr: list, cmp: Callable, idx_l: int, idx_r: int) -> int:
    pivot = arr[random.randint(idx_l, idx_r)]

    lp = idx_l
    rp = idx_r

    while lp <= rp:
        if cmp(arr[lp], pivot) > 0 >= cmp(arr[rp], pivot):
            arr[lp], arr[rp] = arr[rp], arr[lp]
            lp += 1
            rp -= 1

        if cmp(arr[lp], pivot) <= 0:
            lp += 1

        if cmp(arr[rp], pivot) > 0:
            rp -= 1

    return lp


@dataclass
@functools.total_ordering
class UserResult:
    login: str
    score: int
    penalty: int

    def __eq__(self, other: 'UserResult') -> bool:
        return self.login == other.login and self.score == other.score and self.penalty == other.penalty

    def __lt__(self, other: 'UserResult') -> bool:
        if self.score > other.score:
            return False
        elif self.score < other.score:
            return True

        if self.penalty < other.penalty:
            return False
        elif self.penalty > other.penalty:
            return True

        if self.login < other.login:
            return False
        elif self.login > other.login:
            return True
        else:
            return False


def main():
    n = int(input())
    arr: list['UserResult'] = []
    for _ in range(n):
        val = input().split()
        arr.append(UserResult(val[0], int(val[1]), int(val[2])))

    quick_sort(arr, lambda x, y: x < y)

    for el in arr:
        print(el.login)


if __name__ == '__main__':
    main()
