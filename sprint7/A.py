def main():
    n = int(input())
    prices = list(map(int, input().split()))

    max_profit = 0
    for i in range(1, n):
        if prices[i] > prices[i - 1]:
            max_profit += prices[i] - prices[i - 1]

    print(max_profit)


if __name__ == '__main__':
    main()
