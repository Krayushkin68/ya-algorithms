"""
Реализуйте класс StackMaxEffective, поддерживающий операцию определения максимума среди элементов в стеке. Сложность операции должна быть O(1). Для пустого стека операция должна возвращать None. При этом push(x) и pop() также должны выполняться за константное время.

Формат ввода
В первой строке записано одно число — количество команд, оно не превосходит 100000. Далее идут команды по одной в строке. Команды могут быть следующих видов:

push(x) — добавить число x в стек. Число x не превышает 105;
pop() — удалить число с вершины стека;
get_max() — напечатать максимальное число в стеке;
top() — напечатать число с вершины стека;
Если стек пуст, при вызове команды get_max нужно напечатать «None», для команды pop и top — «error».
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


class StackMaxEffective:
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

    def pop(self) -> int:
        if len(self.items) == 0:
            raise Exception()

        value = self.items.pop()

        if value == self.max_items[-1]:
            self.max_items.pop()

        return value

    def top(self) -> int:
        if len(self.items) == 0:
            raise Exception()

        return self.items[-1]


def main():
    commands_count = int(input())

    stack = StackMaxEffective()

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
            elif command.startswith('top'):
                print(stack.top())
        except Exception:
            print("error")


if __name__ == '__main__':
    main()
