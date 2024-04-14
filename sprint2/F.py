"""
Нужно реализовать класс StackMax, который поддерживает операцию определения максимума среди всех элементов в стеке. Класс должен поддерживать операции push(x), где x – целое число, pop() и get_max().

Формат ввода
В первой строке записано одно число n — количество команд, которое не превосходит 10000. В следующих n строках идут команды. Команды могут быть следующих видов:

push(x) — добавить число x в стек. Число x не превышает 105;
pop() — удалить число с вершины стека;
get_max() — напечатать максимальное число в стеке;
Если стек пуст, при вызове команды get_max() нужно напечатать «None», для команды pop() — «error».

Формат вывода
Для каждой команды get_max() напечатайте результат её выполнения. Если стек пустой, для команды get_max() напечатайте «None». Если происходит удаление из пустого стека — напечатайте «error».

Input:
8
get_max
push 7
pop
push -2
push -1
pop
get_max
get_max

Output:
None
-2
-2


"""


class StackMax:
    def __init__(self):
        self.items: list[int] = []
        self.max_items: list[int] = []

    def get_max(self):
        if len(self.max_items) == 0:
            return None

        return self.max_items[-1]

    def push(self, value: int):
        self.items.append(value)

        if len(self.max_items) == 0 or value >= self.max_items[-1]:
            self.max_items.append(value)

    def pop(self):
        if len(self.items) == 0:
            raise Exception()

        value = self.items.pop()

        if value == self.max_items[-1]:
            self.max_items.pop()

        return value


def main():
    commands_count = int(input())

    stack = StackMax()

    for _ in range(commands_count):
        command = input()

        try:
            if command.startswith('get_max'):
                print(stack.get_max())
            elif command.startswith('push'):
                value = int(command.split()[-1])
                stack.push(value)
            elif command.startswith('pop'):
                stack.pop()
        except Exception:
            print("error")


if __name__ == '__main__':
    main()
