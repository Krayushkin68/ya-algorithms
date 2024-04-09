"""
Помогите Васе понять, будет ли фраза палиндромом. Учитываются только буквы и цифры, заглавные и строчные буквы считаются одинаковыми.

Решение должно работать за O(N), где N — длина строки на входе.

Input:
A man, a plan, a canal: Panama
Output:
True
"""

characters = 'abcdefghijklmnopqrstuvwxyz0123456789'


def is_palindrome(row: str) -> bool:
    stack = []
    for el in row:
        if el.lower() in characters:
            stack.append(el.lower())

    for i in range(len(stack) // 2):
        if stack[i] != stack[len(stack) - 1 - i]:
            return False

    return True


if __name__ == '__main__':
    row = input()
    result = is_palindrome(row)
    print(result)
