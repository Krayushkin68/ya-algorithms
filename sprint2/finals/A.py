"""
https://contest.yandex.ru/contest/22781/run-report/112443319/

Реализация дека на кольцевом буфере.
Для внутреннего хранения объектов используется список с изначально известным размером.
Также хранится информация об индексах начала и конца дека.
Принцип:
При добавлении элементов происходит запись в список по индексу начала либо конца, а затем соответствующий индекс сдвигается по модулю размера дека. (при добавлении первого элемента сдвиг не происходит, чтобы начало и конец указывали на один и тот же элемент).
Удаление аналогично.
При достижении максимального размера, выбрасывается исключение при добавлении новых элементов, так как это приведет к перезаписи старых.

Сложность по памяти: O(m) где m - размер дека;
Вспомогательные переменные добавляют константное значение, так как не зависят от размера дека.

Сложность по времени всех операций: O(1);
В каждой операции используются только операции обращения/изменения объекта в списке по индексу - сложность O(1), а также базовые арифметические операции, которые имеют сложность O(1).
Так как размер внутреннего списка фиксирован, дополнительных аллокаций также не будет.

Сложность по времени всей программы: O(n), где n - количество операций с деком;
"""


class DequeEmptyException(Exception):
    pass


class DequeFullException(Exception):
    pass


class Deque:
    def __init__(self, max_size: int):
        self._max_size = max_size
        self._data: list[int] = [-1] * max_size
        self._size: int = 0
        self._front: int = 0
        self._back: int = 0

    def pop_front(self) -> int:
        if self._size == 0:
            raise DequeEmptyException()

        value = self._data[self._front]
        self._size -= 1

        if self._size != 0:
            self._front = (self._front + 1) % self._max_size

        return value

    def pop_back(self) -> int:
        if self._size == 0:
            raise DequeEmptyException()

        value = self._data[self._back]
        self._size -= 1

        if self._size != 0:
            self._back = (self._back - 1) % self._max_size

        return value

    def push_back(self, value):
        if self._size == self._max_size:
            raise DequeFullException()

        if self._size != 0:
            self._back = (self._back + 1) % self._max_size

        self._data[self._back] = value
        self._size += 1

    def push_front(self, value):
        if self._size == self._max_size:
            raise DequeFullException()

        if self._size != 0:
            self._front = (self._front - 1) % self._max_size

        self._data[self._front] = value
        self._size += 1


def main():
    commands_count = int(input())
    deque_max_size = int(input())

    deque = Deque(deque_max_size)

    outputs = []
    for _ in range(commands_count):
        command = input()

        try:
            if command.startswith('pop_front'):
                value = deque.pop_front()
                outputs.append(value)
            elif command.startswith('pop_back'):
                value = deque.pop_back()
                outputs.append(value)
            elif command.startswith('push_front'):
                value = int(command.split()[-1])
                deque.push_front(value)
            elif command.startswith('push_back'):
                value = int(command.split()[-1])
                deque.push_back(value)
        except (DequeEmptyException, DequeFullException):
            outputs.append("error")

    print('\n'.join(map(str, outputs)))


if __name__ == '__main__':
    main()
