"""
Формат ввода
В первой строке дано целое число k (1 ≤ k ≤ 5).

В четырёх следующих строках задан вид тренажёра -— по 4 символа в каждой строке. Каждый символ – либо точка, либо цифра от 1 до 9. Символы одной строки идут подряд и не разделены пробелами.

Формат вывода
Выведите единственное число -— максимальное количество баллов, которое смогут набрать Гоша и Тимофей.

Input:
3
1231
2..2
2..2
2..2

Output:
2
"""


def game(game_field: list[str], k: int) -> int:
    score = 0
    numbers = dict.fromkeys('0123456789', 0)

    for row in game_field:
        for el in row:
            if el != '.':
                numbers[el] += 1

    for t in range(10):
        if numbers[str(t)] > 0 and numbers[str(t)] <= 2 * k:
            score += 1

    return score


if __name__ == '__main__':
    k = int(input())
    game_field = []

    for _ in range(4):
        game_field.append(input())

    result = game(game_field, k)
    print(result)
