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

    path = []
    print(dp[0][-1])
    y, x = 0, m - 1
    while True:
        if y == n - 1 and x == 0:
            break

        left_y, left_x = y, x - 1
        left_valid = left_x >= 0

        down_y, down_x = y + 1, x
        down_valid = down_y < n

        if left_valid and down_valid:
            if dp[left_y][left_x] > dp[down_y][down_x]:
                path.append('R')
                x, y = left_x, left_y
            else:
                path.append('U')
                x, y = down_x, down_y
        elif left_valid:
            path.append('R')
            x, y = left_x, left_y
        elif down_valid:
            path.append('U')
            x, y = down_x, down_y

    print(''.join(reversed(path)))


if __name__ == '__main__':
    main()
