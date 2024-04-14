def transpose(rows: int, cols: int, matrix: list[list[int]]) -> list[list[int]]:
    new_matrix = [[0] * rows for _ in range(cols)]
    for i in range(rows):
        for j in range(cols):
            new_matrix[j][i] = matrix[i][j]

    return new_matrix


def main():
    rows = int(input())
    cols = int(input())

    matrix = []
    for _ in range(rows):
        matrix.append(list(map(int, input().split())))

    result = transpose(rows, cols, matrix)
    for row in result:
        print(' '.join(map(str, row)))


if __name__ == '__main__':
    main()
