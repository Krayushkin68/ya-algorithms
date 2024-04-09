"""
Дана матрица. Нужно написать функцию, которая для элемента возвращает всех его соседей.
Соседним считается элемент, находящийся от текущего на одну ячейку влево, вправо, вверх или вниз.
Диагональные элементы соседними не считаются.

Формат ввода
В первой строке задано n — количество строк матрицы. Во второй — количество столбцов m. Числа m и n не превосходят 1000.
В следующих n строках задана матрица. Элементы матрицы — целые числа, по модулю не превосходящие 1000.
В последних двух строках записаны координаты элемента, соседей которого нужно найти. Индексация начинается с нуля.

Input:
4
3
1 2 3
0 2 6
7 4 1
2 7 0
3
0

Output:
7 7
"""


def get_neighbors(matrix: list[list[int]], row: int, col: int) -> list[int]:
    neighbors = []

    if len(matrix) == 0:
        return neighbors

    if row > len(matrix) - 1 or row < 0 or col < 0 or col > len(matrix[0]) - 1:
        return neighbors

    # upper
    if row > 0:
        neighbors.append(matrix[row - 1][col])

    # lower
    if row < len(matrix) - 1:
        neighbors.append(matrix[row + 1][col])

    # left
    if col > 0:
        neighbors.append(matrix[row][col - 1])

    # right
    if col < len(matrix[0]) - 1:
        neighbors.append(matrix[row][col + 1])

    neighbors.sort()

    return neighbors


if __name__ == '__main__':
    rows = int(input())
    cols = int(input())

    matrix = []
    for _ in range(rows):
        matrix.append(list(map(int, input().split())))

    target_row = int(input())
    target_col = int(input())

    neighbors = get_neighbors(matrix, target_row, target_col)
    print(' '.join(map(str, neighbors)))
