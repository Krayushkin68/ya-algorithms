import os

LOCAL = os.environ.get('REMOTE_JUDGE', 'false') != 'true'

if LOCAL:
    class Node:
        def __init__(self, value, left=None, right=None):
            self.value = value
            self.right = right
            self.left = left


def solution(root) -> int:
    to_visit = [root]
    max_value = None

    while len(to_visit) > 0:
        current = to_visit.pop()
        if max_value is None or current.value > max_value:
            max_value = current.value

        if current.right is not None:
            to_visit.append(current.right)

        if current.left is not None:
            to_visit.append(current.left)

    return max_value


def test():
    node1 = Node(1)
    node2 = Node(-5)
    node3 = Node(3, node1, node2)
    node4 = Node(2, node3, None)
    assert solution(node4) == 3


if __name__ == '__main__':
    test()
