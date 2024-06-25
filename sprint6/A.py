"""
Формат ввода
В первой строке дано число вершин n (1 ≤ n ≤ 100) и число ребер m (1 ≤ m ≤ n(n-1)). В следующих m строках заданы ребра в виде пар вершин (u,v), если ребро ведет от u к v.

Формат вывода
Выведите информацию о рёбрах, исходящих из каждой вершины.

В строке i надо написать число рёбер, исходящих из вершины i, а затем перечислить вершины, в которые ведут эти рёбра –— в порядке возрастания их номеров.
"""


def main():
    verticals, edges = map(int, input().split())

    adj_list = [[] for _ in range(verticals)]

    for _ in range(edges):
        v_from, v_to = map(int, input().split())
        adj_list[v_from - 1].append(v_to)

    outputs = []
    for ix, v_list in enumerate(adj_list):
        outputs.append(f"{len(v_list)} {' '.join(map(str, v_list))}")

    print('\n'.join(outputs))


if __name__ == '__main__':
    main()
