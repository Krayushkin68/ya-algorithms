def format_number(num):
    if num.is_integer():
        return f"{int(num)}"
    else:
        return f"{num:.2f}".rstrip('0').rstrip('.')


def main():
    n = int(input())
    classes = []
    for _ in range(n):
        start, end = input().split()
        classes.append((float(start), float(end)))

    scheduled = []
    for start, end in sorted(classes, key=lambda x: (x[1], x[0])):
        if len(scheduled) == 0:
            scheduled.append((start, end))
            continue

        if start >= scheduled[-1][1]:
            scheduled.append((start, end))

    print(len(scheduled))
    print('\n'.join(f'{format_number(start)} {format_number(end)}' for start, end in scheduled))


if __name__ == '__main__':
    main()
