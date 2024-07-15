def main():
    n, k = map(int, input().split())
    mod = 10 ** 9 + 7

    dp = {1: 1, 2: 1}
    for i in range(3, n + 1):
        dp[i] = 0
        for j in range(1, k + 1):
            if i - j < 1:
                continue

            dp[i] = (dp[i] + dp[i - j]) % mod

    print(dp[n])


if __name__ == '__main__':
    main()
