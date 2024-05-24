import os

LOCAL = os.environ.get('REMOTE_JUDGE', 'false') != 'true'

if LOCAL:
    class Node:
        def __init__(self, value, left=None, right=None):
            self.value = value
            self.right = right
            self.left = left


def solution(root) -> bool:
    to_visit = [(root, None, None)]

    while len(to_visit) > 0:
        current, min_v, max_v = to_visit.pop()
        if min_v is not None and current.value <= min_v:
            return False

        if max_v is not None and current.value >= max_v:
            return False

        if current.right is not None:
            to_visit.append((current.right, current.value, max_v))

        if current.left is not None:
            to_visit.append((current.left, min_v, current.value))

    return True


def test():
    node1 = Node(1, None, None)
    node2 = Node(4, None, None)
    node3 = Node(3, node1, node2)
    node4 = Node(8, None, None)
    node5 = Node(5, node3, node4)

    # assert solution(node5)
    node2.value = 6
    assert not solution(node5)


if __name__ == '__main__':
    test()
