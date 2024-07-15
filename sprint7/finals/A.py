"""
https://contest.yandex.ru/contest/25597/run-report/116325490/

Реализация алгоритма нахождения расстояния Левенштейна с использованием динамического программирования.

Описание алгоритма ДП:
    dp - двумерный массив, ячейка dp[i][j] хранит минимальное количество операций для преобразования строки s1[:i] в строку s2[:j]
    базовый случай - используются дополнительный столбец и строка dp[i][0] = i, dp[0][j] = j - заполняются по возрастанию, это обозначает количество необходимых вставок для преобразования в пустую строку

    переход динамики - при переходе удлиняем одну из подстрок на один символ, при этом возможны три варианта преобразования:
                       1. Удаление символа, тогда dp[i][j] = dp[i - 1][j] + 1;
                       2. Вставка символа, тогда dp[i][j] = dp[i][j - 1] + 1;
                       3. Замена символа, тогда dp[i][j] = dp[i - 1][j - 1] + cost, где cost = 0, если символы равны, иначе 1;
                       Из трех вариантов выбираем наименьший.

Для оптимизации по памяти будем хранить только две последние строки массива dp.
Обмен строк осуществляется по ссылкам, чтобы избежать копирования списков.


Сложность по времени O(|s| * |t|), так как для каждого префикса строки s мы проходим по всем префиксам строки t.
Сложность по памяти O(|t|), так как храним только две последние строки dp, длина строки равна длине строки t.
"""


def levenshtein(s1: str, s2: str) -> int:
    n, m = len(s1), len(s2)

    dp_prev = [j for j in range(m + 1)]
    dp_cur = [0] * (m + 1)

    for i in range(1, n + 1):
        dp_cur[0] = i
        for j in range(1, m + 1):
            dp_cur[j] = min(
                dp_prev[j] + 1,
                dp_cur[j - 1] + 1,
                dp_prev[j - 1] + int(s1[i - 1] != s2[j - 1])
            )

        dp_prev, dp_cur = dp_cur, dp_prev

    return dp_prev[-1]


def main():
    s = input()
    t = input()

    print(levenshtein(s, t))


if __name__ == '__main__':
    main()