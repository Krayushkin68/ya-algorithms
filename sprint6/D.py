"""
Задан неориентированный граф. Обойдите поиском в ширину все вершины, достижимые из заданной вершины s, и выведите их в порядке обхода, если начинать обход из s.

Формат ввода
В первой строке дано количество вершин n (1 ≤ n ≤ 105) и рёбер m (0 ≤ m ≤ 105). Далее в m строках описаны рёбра графа. Каждое ребро описывается номерами двух вершин u и v (1 ≤ u, v ≤ n). В последней строке дан номер стартовой вершины s (1 ≤ s ≤ n).

Гарантируется, что в графе нет петель и кратных рёбер.

Формат вывода
Выведите вершины в порядке обхода, считая что при запуске от каждой конкретной вершины её соседи будут рассматриваться в порядке возрастания (то есть если вершина 2 соединена с 1 и 3, то сначала обход пойдёт в 1, а уже потом в 3).
"""
from queue import Queue


def bfs(vertex_num: int, adj_list: list, start_v: int):
    planned = Queue()
    colors = ['white'] * vertex_num
    visited_order = []

    planned.put(start_v)
    while not planned.empty():
        v = planned.get()
        visited_order.append(str(v + 1))
        colors[v] = 'gray'

        for sibling in sorted(adj_list[v]):
            if colors[sibling] == 'white':
                colors[sibling] = 'gray'
                planned.put(sibling)

        colors[v] = 'black'

    return visited_order


def main():
    vertex_num, edges_num = map(int, input().split())

    adj_list = [[] for _ in range(vertex_num)]

    for _ in range(edges_num):
        v_from, v_to = map(int, input().split())
        adj_list[v_from - 1].append(v_to - 1)
        adj_list[v_to - 1].append(v_from - 1)

    start_v = int(input()) - 1

    visited = bfs(vertex_num, adj_list, start_v)
    print(' '.join(visited))


if __name__ == '__main__':
    main()
