"""
https://contest.yandex.ru/contest/25070/run-report/115786916/

Реализация алгоритма Прима для нахождения максимального остовного дерева в неориентированном взвешенном графе.
Хранение списка рёбер осуществляется с помощью приоритетной очереди (модуль heapq, в котором используются инвертированные веса с целью имитации работы кучи на максимум).

Временная сложность (в худшем случае):
    Построение списка смежности: O(E), так как граф вводится в виде списка рёбер.
    Построение максимального остовного дерева: O(E * log(V)), так как операции добавления/удаления элементов в приоритетной очереди выполняются за O(log(k)), где k - количество элементов в куче.
    Общая сложность программы: O(E * log(V)).

Пространственная сложность (в худшем случае):
    Хранение графа в виде списка смежности: O(V + E).
    Хранение множества посещённых вершин: O(V).
    Хранение приоритетной очереди: O(E).
    Общая сложность программы: O(V + E).
"""

import heapq


class MultipleComponentsException(Exception):
    pass


def prim(adj_list: list) -> int:
    mst_weight = 0
    visited = set()
    edges = [(0, 0, None)]

    while edges:
        weight, current_vertex, previous_vertex = heapq.heappop(edges)

        if current_vertex not in visited:
            visited.add(current_vertex)

            if previous_vertex is not None:
                mst_weight += -weight

            for neighbor, edge_weight in adj_list[current_vertex]:
                if neighbor not in visited:
                    heapq.heappush(edges, (-edge_weight, neighbor, current_vertex))

    if len(visited) != len(adj_list):
        raise MultipleComponentsException('Graph has multiple connectivity components')

    return mst_weight


def main():
    vertex_num, edges_num = map(int, input().split())

    adj_list = [[] for _ in range(vertex_num)]

    for _ in range(edges_num):
        v_from, v_to, weight = map(int, input().split())
        adj_list[v_from - 1].append((v_to - 1, weight))
        adj_list[v_to - 1].append((v_from - 1, weight))

    try:
        res = prim(adj_list)
        print(res)
    except MultipleComponentsException:
        print('Oops! I did it again')


if __name__ == '__main__':
    main()
