"""
Формат ввода
В первой строке дано число вершин n (1 ≤ n ≤ 2⋅ 105) и рёбер (0 ≤ m ≤ 2 ⋅ 105). В каждой из следующих m строк записаны рёбра графа в виде пар (from, to), 1 ≤ from ≤ n — начало ребра, 1 ≤ to ≤ n — его конец. Гарантируется, что в графе нет петель и кратных рёбер.

Формат вывода
Выведите n строк, в каждой из которых записана пара чисел tini, touti — время входа и выхода для вершины i.
"""


def dfs(vertex_num: int, adj_list: list, start_v: int):
    stack = [start_v]
    colors = ['white'] * vertex_num
    times = [[-1, -1] for _ in range(vertex_num)]
    time = -1

    while stack:
        v = stack.pop()

        if colors[v] == 'white':
            time += 1
            times[v][0] = time
            colors[v] = 'grey'
            stack.append(v)

            for sibling in sorted(adj_list[v], reverse=True):
                if colors[sibling] == 'white':
                    stack.append(sibling)
        elif colors[v] == 'grey':
            time += 1
            times[v][1] = time
            colors[v] = 'black'

    return times


def main():
    vertex_num, edges_num = map(int, input().split())

    adj_list = [[] for _ in range(vertex_num)]

    for _ in range(edges_num):
        v_from, v_to = map(int, input().split())
        adj_list[v_from - 1].append(v_to - 1)

    times = dfs(vertex_num, adj_list, 0)
    print('\n'.join(f'{t_in} {t_out}' for t_in, t_out in times))


if __name__ == '__main__':
    main()
