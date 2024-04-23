def sort_bubble(values: list[int]) -> list[int]:
    was_sorted = True
    for _ in range(len(values) - 1):
        changed = False
        for i in range(len(values) - 1):
            if values[i] > values[i + 1]:
                values[i], values[i + 1] = values[i + 1], values[i]
                changed = True
                was_sorted = False

        if changed:
            print(' '.join(map(str, values)))

    if was_sorted:
        print(' '.join(map(str, values)))

    return values


def main():
    n = int(input())
    values = list(map(int, input().split()))
    sorted_values = sort_bubble(values)


if __name__ == '__main__':
    main()
