def sift_down(heap, idx) -> int:
    value = heap[idx]

    child_idx_l = 2 * idx
    child_idx_r = 2 * idx + 1

    if child_idx_l < len(heap) and child_idx_r < len(heap):
        # both active
        l_value = heap[child_idx_l]
        r_value = heap[child_idx_r]

        if max(l_value, r_value) > value:
            if l_value >= r_value:
                heap[idx], heap[child_idx_l] = heap[child_idx_l], heap[idx]
                return sift_down(heap, child_idx_l)
            else:
                heap[idx], heap[child_idx_r] = heap[child_idx_r], heap[idx]
                return sift_down(heap, child_idx_r)
        else:
            return idx

    elif child_idx_l < len(heap):
        # only left
        l_value = heap[child_idx_l]

        if l_value > value:
            heap[idx], heap[child_idx_l] = heap[child_idx_l], heap[idx]
            return sift_down(heap, child_idx_l)
        else:
            return idx
    elif child_idx_r < len(heap):
        # only right
        r_value = heap[child_idx_r]

        if r_value > value:
            heap[idx], heap[child_idx_r] = heap[child_idx_r], heap[idx]
            return sift_down(heap, child_idx_r)
        else:
            return idx
    else:
        return idx


def test():
    sample = [-1, 12, 1, 8, 3, 4, 7]
    # print(sift_down(sample, 2))
    assert sift_down(sample, 2) == 5


if __name__ == '__main__':
    test()
