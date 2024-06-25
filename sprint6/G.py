"""
Под расстоянием между двумя вершинами в графе будем понимать длину кратчайшего пути между ними в рёбрах. Для данной вершины s определите максимальное расстояние от неё до другой вершины неориентированного графа.

Выведите длину наибольшего пути от s до одной из вершин графа.
"""
from queue import Queue
from typing import Union, List


def bfs(vertex_num: int, adj_list: list, start_v: int):
    planned = Queue()
    colors = ['white'] * vertex_num
    distance: List[Union[int, None]] = [None] * vertex_num
    previous: List[Union[int, None]] = [None] * vertex_num

    planned.put(start_v)
    distance[start_v] = 0

    while not planned.empty():
        v = planned.get()
        colors[v] = 'gray'

        for sibling in sorted(adj_list[v]):
            if colors[sibling] == 'white':
                previous[sibling] = v
                distance[sibling] = distance[v] + 1
                colors[sibling] = 'gray'
                planned.put(sibling)

        colors[v] = 'black'

    return distance


def main():
    vertex_num, edges_num = map(int, input().split())

    adj_list = [[] for _ in range(vertex_num)]

    for _ in range(edges_num):
        v_from, v_to = map(int, input().split())
        adj_list[v_from - 1].append(v_to - 1)
        adj_list[v_to - 1].append(v_from - 1)

    start_v = int(input()) - 1

    distances = bfs(vertex_num, adj_list, start_v)
    print(max(distances))


if __name__ == '__main__':
    main()
