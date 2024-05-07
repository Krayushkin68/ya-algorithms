"""
Жители Алгосского архипелага придумали новый способ сравнения строк. Две строки считаются равными,
если символы одной из них можно заменить на символы другой так, что первая строка станет точной копией второй строки.
При этом необходимо соблюдение двух условий:

Порядок вхождения символов должен быть сохранён.
Одинаковым символам первой строки должны соответствовать одинаковые символы второй строки. Разным символам —– разные.
Например, если строка s = «abacaba», то ей будет равна строка t = «xhxixhx», так как все вхождения «a» заменены на «x», «b» –— на «h», а «c» –— на «i».
Если же первая строка s=«abc», а вторая t=«aaa», то строки уже не будут равны, так как разные буквы первой строки соответствуют одинаковым буквам второй.

Формат ввода
В первой строке записана строка s, во второй –— строка t. Длины обеих строк не превосходят 106. Обе строки содержат хотя бы по одному символу и состоят только из маленьких латинских букв.

Строки могут быть разной длины.

Формат вывода
Выведите «YES», если строки равны (согласно вышеописанным правилам), и «NO» в ином случае.

Input:
mxyskaoghi
qodfrgmslc

Output:
YES

Input:
agg
xda

Output:
NO
"""

from string import ascii_lowercase


def to_common_alphabet(string: str) -> str:
    alphabet = ascii_lowercase
    char_map = {}
    last_char_idx = 0
    converted = []

    for char in string:
        if char not in char_map:
            char_map[char] = alphabet[last_char_idx]
            last_char_idx += 1

        converted.append(char_map[char])

    return ''.join(converted)


def is_equal(s: str, t: str) -> bool:
    return to_common_alphabet(s) == to_common_alphabet(t)


def main():
    s = input()
    t = input()

    res = is_equal(s, t)
    print('YES' if res else 'NO')


if __name__ == '__main__':
    main()
