"""
Любимый вариант очереди Тимофея — очередь, написанная с использованием связного списка. Помогите ему с реализацией. Очередь должна поддерживать выполнение трёх команд:

get() — вывести элемент, находящийся в голове очереди, и удалить его. Если очередь пуста, то вывести «error».
put(x) — добавить число x в очередь
size() — вывести текущий размер очереди
Формат ввода
В первой строке записано количество команд n — целое число, не превосходящее 1000. В каждой из следующих n строк записаны команды по одной строке.

Формат вывода
Выведите ответ на каждый запрос по одному в строке.

Input:
10
put -34
put -23
get
size
get
size
get
get
put 80
size

Output:
-34
1
-23
0
error
error
1


"""
from queue import Empty
from typing import Union


class Node:
    def __init__(self, data: int, left=None, right=None):
        self.data = data
        self.left = left
        self.right = right


class Queue:
    def __init__(self):
        self.head: Union[Node, None] = None
        self.tail: Union[Node, None] = None
        self._size: int = 0

    def get(self) -> int:
        if self._size == 0:
            raise Empty('Queue is empty')

        value = self.head.data
        self.head = self.head.right
        self._size -= 1

        if self._size == 0:
            self.tail = None

        return value

    def put(self, value):
        node = Node(value)

        if self._size == 0:
            self.head = node
            self.tail = node
        else:
            self.tail.right = node
            self.tail = node

        self._size += 1

    def size(self) -> int:
        return self._size


def main():
    commands_count = int(input())

    queue = Queue()

    for _ in range(commands_count):
        command = input()

        try:
            if command.startswith('get'):
                print(queue.get())
            elif command.startswith('put'):
                value = int(command.split()[-1])
                queue.put(value)
            elif command.startswith('size'):
                print(queue.size())
        except Exception:
            print("error")


if __name__ == '__main__':
    main()
