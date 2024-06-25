"""
Вам дан неориентированный граф. Найдите его компоненты связности.

Формат ввода
В первой строке дано количество вершин n (1≤ n ≤ 105) и рёбер m (0 ≤ m ≤ 2 ⋅ 105). В каждой из следующих m строк записано по ребру в виде пары вершин 1 ≤ u, v ≤ n.

Гарантируется, что в графе нет петель и кратных рёбер.

Формат вывода
Выведите все компоненты связности в следующем формате: в первой строке выведите общее количество компонент.

Затем на отдельных строках выведите вершины каждой компоненты, отсортированные по возрастанию номеров. Компоненты между собой упорядочивайте по номеру первой вершины.
"""


def dfs(vertex_num: int, adj_list: list):
    stack = []
    colors = ['white'] * vertex_num

    comp_colors = {}
    current_color = 0

    for start_v in range(vertex_num):
        if colors[start_v] == 'white':
            current_color += 1  # new component
            comp_colors[current_color] = []
            stack.append(start_v)

        while stack:
            v = stack.pop()

            if colors[v] == 'white':
                colors[v] = 'grey'
                comp_colors[current_color].append(v + 1)
                stack.append(v)

                for sibling in sorted(adj_list[v], reverse=True):
                    if colors[sibling] == 'white':
                        stack.append(sibling)
            elif colors[v] == 'grey':
                colors[v] = 'black'

    return comp_colors


def main():
    vertex_num, edges_num = map(int, input().split())

    adj_list = [[] for _ in range(vertex_num)]

    for _ in range(edges_num):
        v_from, v_to = map(int, input().split())
        adj_list[v_from - 1].append(v_to - 1)
        adj_list[v_to - 1].append(v_from - 1)

    comp_colors = dfs(vertex_num, adj_list)
    print(len(comp_colors.keys()))
    lists = sorted((sorted(el) for el in comp_colors.values()), key=lambda x: x[0])
    print('\n'.join(' '.join(map(str, l)) for l in lists))


if __name__ == '__main__':
    main()
