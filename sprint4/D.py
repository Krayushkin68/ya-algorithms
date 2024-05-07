def hash_str(string: str, base: int, mod: int) -> int:
    if len(string) == 0:
        return 0

    result = 0

    result += ord(string[0])
    for i, char in enumerate(string[1:]):
        result = (result * base + ord(char)) % mod

    return result


def main():
    a = int(input())
    m = int(input())
    s = input()

    res = hash_str(s, a, m)
    print(res)


if __name__ == '__main__':
    main()
