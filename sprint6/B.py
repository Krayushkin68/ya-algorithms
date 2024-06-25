"""
Формат ввода
В первой строке дано число вершин n (1 ≤ n ≤ 100) и число рёбер m (1 ≤ m ≤ n(n-1)). В следующих m строках заданы ребра в виде пар вершин (u,v), если ребро ведет от u к v.

Формат вывода
Выведите матрицу смежности n на n. На пересечении i-й строки и j-го столбца стоит единица, если есть ребро, ведущее из i в j.
"""


def main():
    verticals, edges = map(int, input().split())

    matrix = [[0 for _ in range(verticals)] for _ in range(verticals)]

    for _ in range(edges):
        v_from, v_to = map(int, input().split())
        matrix[v_from - 1][v_to - 1] = 1

    outputs = []
    for row in matrix:
        outputs.append(' '.join(map(str, row)))

    print('\n'.join(outputs))


if __name__ == '__main__':
    main()
