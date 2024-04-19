"""
https://contest.yandex.ru/contest/22781/run-report/112444646/

Реализация калькулятора выражения в постфиксной нотации.
Принцип:
Задаем что считаем операндом, а что операцией. В данном случае все операции бинарные.
Последовательно проходим по каждому элементу, операнды кладем в стек, а операции выполняем для последних двух операндов в стеке, возвращая результат в стек.
Итоговый результат будет единственным элементом в стеке.

Сложность по памяти: в худшем случае O(n), где n - количество элементов в выражении; так как для хранения операндов и промежуточных вычислений используется стек.

Сложность по времени: O(n), где n - количество элементов в выражении; так как происходит последовательный проход по каждому элементу.
"""


def calculator(operations: list[str]) -> int:
    stack: list[int] = []

    operators = {
        '+': lambda x, y: x + y,
        '-': lambda x, y: x - y,
        '*': lambda x, y: x * y,
        '/': lambda x, y: x // y,
    }

    for el in operations:
        if el in operators:
            operand_right = stack.pop()
            operand_left = stack.pop()
            result = operators[el](operand_left, operand_right)
            stack.append(result)
        else:
            stack.append(int(el))

    return stack.pop()


def main():
    operations = input().split()
    result = calculator(operations)
    print(result)


if __name__ == '__main__':
    main()
