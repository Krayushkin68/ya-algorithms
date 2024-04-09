"""
Чтобы подготовиться к семинару, Гоше надо прочитать статью по эффективному менеджменту. Так как Гоша хочет спланировать день заранее, ему необходимо оценить сложность статьи.

Он придумал такой метод оценки: берётся случайное предложение из текста и в нём ищется самое длинное слово. Его длина и будет условной сложностью статьи.

Помогите Гоше справиться с этой задачей.

Формат ввода
В первой строке дана длина текста L (1 ≤ L ≤ 105).

В следующей строке записан текст, состоящий из строчных латинских букв и пробелов. Слово —– последовательность букв, не разделённых пробелами. Пробелы могут стоять в самом начале строки и в самом её конце. Текст заканчивается переносом строки, этот символ не включается в число остальных L символов.

Формат вывода
В первой строке выведите самое длинное слово. Во второй строке выведите его длину. Если подходящих слов несколько, выведите то, которое встречается раньше.

Input:
19
i love segment tree

Output:
segment
7
"""


def get_longest_word(row: str) -> str:
    first_letter_idx = None
    is_in_word = False
    longest_word = ''
    row += ' '
    for i in range(len(row)):
        if row[i] == ' ':
            if not is_in_word:
                continue

            if i - first_letter_idx > len(longest_word):
                longest_word = row[first_letter_idx:i]

            is_in_word = False
        else:
            if not is_in_word:
                first_letter_idx = i
                is_in_word = True

    return longest_word


if __name__ == '__main__':
    n = int(input())
    row = input()

    result = get_longest_word(row)

    print(result)
    print(len(result))
