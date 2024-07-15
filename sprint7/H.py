def main():
    n, m = map(int, input().split())

    matrix = []
    for _ in range(n):
        matrix.append(list(map(int, list(input()))))

    dp = [[0] * m for _ in range(n)]
    dp[n - 1][0] = matrix[n - 1][0]

    for y in range(n - 1, -1, -1):
        for x in range(m):
            from_left = dp[y][x - 1] if x - 1 >= 0 else 0
            from_down = dp[y + 1][x] if y + 1 < n else 0
            dp[y][x] = max(from_left, from_down) + matrix[y][x]

    print(dp[0][-1])


if __name__ == '__main__':
    main()
