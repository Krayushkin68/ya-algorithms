"""
Задан неориентированный граф. Обойдите с помощью DFS все вершины, достижимые из заданной вершины s, и выведите их в порядке обхода, если начинать обход из s.

Формат ввода
В первой строке дано количество вершин n (1 ≤ n ≤ 105) и рёбер m (0 ≤ m ≤ 105). Далее в m строках описаны рёбра графа. Каждое ребро описывается номерами двух вершин u и v (1 ≤ u, v ≤ n). В последней строке дан номер стартовой вершины s (1 ≤ s ≤ n). В графе нет петель и кратных рёбер.

Формат вывода
Выведите вершины в порядке обхода, считая что при запуске от каждой конкретной вершины её соседи будут рассматриваться в порядке возрастания (то есть если вершина 2 соединена с 1 и 3, то сначала обход пойдёт в 1, а уже потом в 3).
"""


def dfs(vertex_num: int, adj_list: list, start_v: int):
    stack = [start_v]
    colors = ['white'] * vertex_num

    while stack:
        v = stack.pop()

        if colors[v] == 'white':
            print(v + 1)
            colors[v] = 'grey'
            stack.append(v)

            for sibling in sorted(adj_list[v], reverse=True):
                if colors[sibling] == 'white':
                    stack.append(sibling)
        elif colors[v] == 'grey':
            colors[v] = 'black'


def main():
    vertex_num, edges_num = map(int, input().split())

    adj_list = [[] for _ in range(vertex_num)]

    for _ in range(edges_num):
        v_from, v_to = map(int, input().split())
        adj_list[v_from - 1].append(v_to - 1)
        adj_list[v_to - 1].append(v_from - 1)

    start_v = int(input())
    dfs(vertex_num, adj_list, start_v - 1)


if __name__ == '__main__':
    main()
