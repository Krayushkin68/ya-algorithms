"""
Дан ациклический ориентированный граф (так называемый DAG, directed acyclic graph).
Найдите его топологическую сортировку, то есть выведите его вершины в таком порядке, что все рёбра графа идут слева направо.
У графа может быть несколько подходящих перестановок вершин. Вам надо найти любую топологическую сортировку.
"""


def topological_sort_dfs(vertex_num: int, adj_list: list):
    stack = []
    colors = ['white'] * vertex_num
    topology_sorted = []

    for start_v in range(vertex_num):
        if colors[start_v] == 'white':
            stack.append(start_v)

        while stack:
            v = stack.pop()

            if colors[v] == 'white':
                colors[v] = 'grey'
                stack.append(v)

                for sibling in sorted(adj_list[v], reverse=True):
                    if colors[sibling] == 'white':
                        stack.append(sibling)
            elif colors[v] == 'grey':
                topology_sorted.append(v + 1)
                colors[v] = 'black'

    return topology_sorted[::-1]


def main():
    vertex_num, edges_num = map(int, input().split())

    adj_list = [[] for _ in range(vertex_num)]

    for _ in range(edges_num):
        v_from, v_to = map(int, input().split())
        adj_list[v_from - 1].append(v_to - 1)

    topology_sorted = topological_sort_dfs(vertex_num, adj_list)
    print(' '.join(map(str, topology_sorted)))


if __name__ == '__main__':
    main()
