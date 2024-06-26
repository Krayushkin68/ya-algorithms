"""
В компании, где работает Тимофей, заботятся о досуге сотрудников и устраивают различные кружки по интересам. Когда кто-то записывается на занятие, в лог вносится название кружка.

По записям в логе составьте список всех кружков, в которые ходит хотя бы один человек.

Формат ввода
В первой строке даётся натуральное число n, не превосходящее 10 000 –— количество записей в логе.

В следующих n строках —– названия кружков.

Формат вывода
Выведите уникальные названия кружков по одному на строке, в порядке появления во входных данных.

Input:
8
вышивание крестиком
рисование мелками на парте
настольный керлинг
настольный керлинг
кухня африканского племени ужасмай
тяжелая атлетика
таракановедение
таракановедение

Output:
вышивание крестиком
рисование мелками на парте
настольный керлинг
кухня африканского племени ужасмай
тяжелая атлетика
таракановедение
"""


def main():
    n = int(input())

    activities = {}
    for _ in range(n):
        activity = input()
        activities[activity] = True

    print('\n'.join(activities.keys()))


if __name__ == '__main__':
    main()
