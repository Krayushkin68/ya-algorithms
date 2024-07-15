def main():
    mod = 10 ** 9 + 7
    n = int(input())

    if n < 2:
        print(1)
        return

    preprev = 1  # n - 2
    prev = 1  # n - 1
    for i in range(2, n + 1):
        cur = (prev + preprev) % mod
        preprev = prev
        prev = cur

    print(prev)


if __name__ == '__main__':
    main()
