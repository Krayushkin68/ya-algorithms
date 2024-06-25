"""
https://contest.yandex.ru/contest/25070/run-report/115792335/

По условию задачи дороги ведут от города с меньшим номеров к городу с большим номером. Это значит, что граф ацикличен.

Идея решения состоит в том, что если мы развернем направления одного из типов дорог (в данном случае 'B') и в полученном графе обнаружим цикл, то дорожная сеть не будет оптимальной.

При наличии цикла необходимо, чтобы между городами X и Y был маршрут как в прямом направлении, так и в обратном.
А так как в прямом направлении идут дороги только типа 'R', а в обратном только типа 'B', то между городами X и Y будут маршруты по дорогам разных типов, что нарушает условие оптимальности.

Для проверки наличия цикла в графе используется алгоритм DFS.

Обозначения:
    V - количество вершин графа, равняется количеству городов n
    E - количество рёбер графа, равняется количеству дорог, в контексте задачи - Σ(n-i), где i от 1 до n - 1

Временная сложность алгоритма:
    Построение списка смежности: O(V + E)
    Сложность алгоритма DFS - O(V + E)
    Общая сложность программы: O(V + E)

Пространственная сложность алгоритма:
    Хранение графа в виде списка смежности: O(V + E)
    Хранение цветов вершин: O(V)
    Хранение стека посещенных вершин: O(V)
    Общая сложность программы: O(V+E)

"""

WHITE = -1
GREY = 0
BLACK = 1


def dfs_check_cycle(adj_list: list):
    stack: list[int] = []
    colors: list[int] = [WHITE] * len(adj_list)

    for start_v in range(len(adj_list)):
        if colors[start_v] == WHITE:
            stack.append(start_v)

        while stack:
            v = stack.pop()

            if colors[v] == WHITE:
                colors[v] = GREY
                stack.append(v)

                for sibling in adj_list[v]:
                    if colors[sibling] == WHITE:
                        stack.append(sibling)
                    elif colors[sibling] == GREY:
                        return True
            elif colors[v] == GREY:
                colors[v] = BLACK

    return False


def main():
    vertex_num = int(input())

    adj_list = [[] for _ in range(vertex_num)]

    for city_num in range(vertex_num - 1):
        roads = list(input())
        for to_city_num, road_type in enumerate(roads):
            if road_type == 'R':
                adj_list[city_num].append(city_num + to_city_num + 1)
            elif road_type == 'B':
                adj_list[city_num + to_city_num + 1].append(city_num)

    if not dfs_check_cycle(adj_list):
        print('YES')
    else:
        print('NO')


if __name__ == '__main__':
    main()
