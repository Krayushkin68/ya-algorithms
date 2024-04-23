def merge(arr, lf, mid, rg):
    array_l = arr[lf:mid]
    array_r = arr[mid:rg]

    idx_l = 0
    idx_r = 0
    idx = 0

    while idx_l < len(array_l) and idx_r < len(array_r):
        if array_l[idx_l] <= array_r[idx_r]:
            arr[lf + idx] = array_l[idx_l]
            idx_l += 1
        else:
            arr[lf + idx] = array_r[idx_r]
            idx_r += 1
        idx += 1

    while idx_l < len(array_l):
        arr[lf + idx] = array_l[idx_l]
        idx_l += 1
        idx += 1

    while idx_r < len(array_r):
        arr[lf + idx] = array_r[idx_r]
        idx_r += 1
        idx += 1

    return arr


def merge_sort(arr, lf, rg):
    if rg - lf <= 1:
        return

    middle = lf + (rg - lf) // 2

    merge_sort(arr, lf, middle)
    merge_sort(arr, middle, rg)

    merge(arr, lf, middle, rg)


def test():
    a = [1, 4, 9, 2, 10, 11]
    b = merge(a, 0, 3, 6)
    expected = [1, 2, 4, 9, 10, 11]
    assert b == expected

    a = [17, 7]
    b = merge(a, 0, 1, 2)
    expected = [7, 17]
    assert b == expected

    c = [1, 4, 2, 10, 1, 2]
    merge_sort(c, 0, 6)
    expected = [1, 1, 2, 2, 4, 10]
    assert c == expected

    c = [1, 4, 2, 10, 1, 2]
    merge_sort(c, 0, 6)
    expected = [1, 1, 2, 2, 4, 10]
    assert c == expected

    c = [-6, -12, -14, 14]
    merge_sort(c, 0, 4)
    expected = [-14, -12, -6, 14]
    assert c == expected


if __name__ == '__main__':
    test()
