def main():
    capacity = int(input())
    n = int(input())

    pieces = []
    for _ in range(n):
        price, weight = list(map(int, input().split()))
        pieces.append((price, weight))

    max_price = 0
    cur_weight = 0
    for price, weight in sorted(pieces, key=lambda x: x[0], reverse=True):
        if cur_weight >= capacity:
            break

        can_take = min(capacity - cur_weight, weight)

        cur_weight += can_take
        max_price += can_take * price

    print(max_price)


if __name__ == '__main__':
    main()
