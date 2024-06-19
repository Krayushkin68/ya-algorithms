"""
https://contest.yandex.ru/contest/24810/run-report/115398567/

Реализация сортировки на основе кучи на максимум (MaxHeap).
Логика сравнения результатов перенесена из финальной задачи B спринта 3 (класс UserResult).

MaxHeap реализован с использованием списка, в котором первый элемент игнорируется для удобства индексации.
Реализованы методы добавления элемента и извлечения максимального элемента.
При добавлении элемента происходит просеивание вверх, при извлечении - просеивание вниз.

Таким образом алгоритм работы программы состоит из двух этапов:
  1. Заполнение кучи результатами
  2. Извлечения из кучи результатов с помощью метода get_max (что и дает результаты, отсортированные по убыванию)

Сложность просеивания вверх и вниз: O(log(n)), так как в худшем случае элемент может пройти по всем уровням дерева
Сложность добавления элемента в кучу: O(log(n)), так как добавление элемента в кучу включает в себя просеивание вверх
Сложность извлечения элемента из кучи: O(log(n)), так как извлечение элемента включает в себя просеивание вниз

Сложность по времени всей программы: O(n*log(n)), так как добавление и извлечение элемента из кучи имеют сложность O(log(n))
Сложность по памяти всей программы: O(n), так как куча использует список для хранения результатов
"""

import functools
from dataclasses import dataclass
from typing import TypeVar, Generic

T = TypeVar('T')


class MaxHeap(Generic[T]):
    def __init__(self):
        self._arr: list[T] = [None]

    def add(self, elem: T):
        self._arr.append(elem)
        self._sift_up(len(self._arr) - 1)

    def get_max(self) -> T:
        if len(self._arr) == 1:
            return None

        value = self._arr[1]
        if len(self._arr) > 2:
            self._arr[1] = self._arr.pop()
            self._sift_down(1)
        elif len(self._arr) == 2:
            self._arr.pop()

        return value

    def _sift_up(self, idx: int):
        parent_idx = idx // 2
        while idx > 1 and self._arr[parent_idx] < self._arr[idx]:
            self._arr[parent_idx], self._arr[idx] = self._arr[idx], self._arr[parent_idx]
            idx //= 2
            parent_idx = idx // 2

    def _sift_down(self, idx: int):
        while 2 * idx < len(self._arr):
            child_idx_l = 2 * idx
            child_idx_r = 2 * idx + 1

            max_child_idx = child_idx_l
            if child_idx_r < len(self._arr) and self._arr[child_idx_r] > self._arr[child_idx_l]:
                max_child_idx = child_idx_r

            if self._arr[idx] >= self._arr[max_child_idx]:
                break

            self._arr[idx], self._arr[max_child_idx] = self._arr[max_child_idx], self._arr[idx]
            idx = max_child_idx


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

    heap = MaxHeap[UserResult]()

    for _ in range(n):
        val = input().split()
        user_result = UserResult(val[0], int(val[1]), int(val[2]))

        heap.add(user_result)

    sorted_results = (heap.get_max().login for _ in range(n))
    print('\n'.join(sorted_results))


if __name__ == '__main__':
    main()
