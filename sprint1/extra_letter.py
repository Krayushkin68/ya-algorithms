"""
Васе очень нравятся задачи про строки, поэтому он придумал свою. Есть 2 строки s и t, состоящие только из строчных букв.
Строка t получена перемешиванием букв строки s и добавлением 1 буквы в случайную позицию. Нужно найти добавленную букву.

Формат ввода
На вход подаются строки s и t, разделённые переносом строки. Длины строк не превосходят 1000 символов. Строки не бывают пустыми.

Input:
abcd
abcde

Output:
e
"""


def get_extra_letter(a: str, b: str) -> str:
    letters = {}

    for i in range(len(b)):
        if i < len(a):
            if a[i] not in letters:
                letters[a[i]] = 1
            else:
                letters[a[i]] += 1

        if b[i] not in letters:
            letters[b[i]] = -1
        else:
            letters[b[i]] -= 1

    for letter, count in letters.items():
        if count != 0:
            return letter


if __name__ == '__main__':
    a = input()
    b = input()

    result = get_extra_letter(a, b)
    print(result)
