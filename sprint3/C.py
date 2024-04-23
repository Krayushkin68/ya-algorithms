"""
Формат ввода
В первой строке записана строка s.

Во второй —- строка t.

Обе строки состоят из маленьких латинских букв, длины строк не превосходят 150000. Строки не могут быть пустыми.

Формат вывода
Выведите True, если s является подпоследовательностью t, иначе —– False.

Input:
abc
ahbgdcu

Output:
True
"""


def is_substr(s: str, t: str) -> bool:
    idx_s = 0
    idx_t = 0

    while idx_s < len(s) and idx_t < len(t):
        if s[idx_s] == t[idx_t]:
            idx_s += 1
        idx_t += 1

    return idx_s == len(s)


def main():
    s = input()
    t = input()

    result = is_substr(s, t)
    print(result)


if __name__ == '__main__':
    main()
