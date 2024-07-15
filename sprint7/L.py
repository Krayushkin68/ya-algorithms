def main():
    n, m = map(int, input().split())
    weights = list(map(int, input().split()))

    dp = [[0] * (m + 1) for _ in range(2)]

    for i in range(n):  # i - number of golden plate
        dp[0] = dp[1]
        dp[1] = [0] * (m + 1)
        for j in range(m + 1):  # j - backpack weight
            if j == 0:
                dp[1][j] = 0
            elif i == 0:
                dp[1][j] = weights[i] if weights[i] <= j else 0
            else:
                previous_top = dp[0][j]
                current_plus_top = weights[i] + dp[0][j - weights[i]] if j - weights[i] >= 0 else 0
                dp[1][j] = max(previous_top, current_plus_top)

    print(dp[-1][-1])


if __name__ == '__main__':
    main()
