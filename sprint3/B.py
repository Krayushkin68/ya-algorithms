"""
На клавиатуре старых мобильных телефонов каждой цифре соответствовало несколько букв. Примерно так:

2:'abc',
3:'def',
4:'ghi',
5:'jkl',
6:'mno',
7:'pqrs',
8:'tuv',
9:'wxyz'

Вам известно в каком порядке были нажаты кнопки телефона, без учета повторов. Напечатайте все комбинации букв, которые можно набрать такой последовательностью нажатий.
Формат ввода
На вход подается строка, состоящая из цифр 2-9 включительно. Длина строки не превосходит 10 символов.

Формат вывода
Выведите все возможные комбинации букв через пробел в лексикографическом (алфавитном) порядке по возрастанию.

Input:
23

Output:
ad ae af bd be bf cd ce cf
"""


def gen_combinations(numbers: str) -> list[str]:
    if len(numbers) == 0:
        return ['']

    combinations = []

    _gen_combinations(numbers, '', 0, combinations)

    return combinations


def _gen_combinations(numbers: str, current: str, idx: int, combinations: list[str]):
    options = {
        2: 'abc',
        3: 'def',
        4: 'ghi',
        5: 'jkl',
        6: 'mno',
        7: 'pqrs',
        8: 'tuv',
        9: 'wxyz'
    }

    if idx == len(numbers):
        combinations.append(current)
        return

    for char in options[int(numbers[idx])]:
        _gen_combinations(numbers, current + char, idx + 1, combinations)


def main():
    numbers = input()
    result = gen_combinations(numbers)

    print(' '.join(result))


if __name__ == '__main__':
    main()
