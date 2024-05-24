import os

LOCAL = os.environ.get('REMOTE_JUDGE', 'false') != 'true'

if LOCAL:
    class Node:
        def __init__(self, value, left=None, right=None):
            self.value = value
            self.right = right
            self.left = left


def solution(root) -> bool:
    to_visit = [root]
    while len(to_visit) > 0:
        current = to_visit.pop(0)

        left_height = get_height(current.left)
        right_height = get_height(current.right)
        if abs(left_height - right_height) > 1:
            return False

        if current.left:
            to_visit.append(current.left)
        if current.right:
            to_visit.append(current.right)

    return True


def get_height(root) -> int:
    if root is None:
        return 0

    current_height = 0
    to_visit = [root]
    while len(to_visit) > 0:
        current_height += 1

        successors = []
        for x in to_visit:
            if x.left is not None:
                successors.append(x.left)
            if x.right is not None:
                successors.append(x.right)

        to_visit = successors

    return current_height


def test():
    node1 = Node(1)
    node2 = Node(-5)
    node3 = Node(3, node1, node2)
    node4 = Node(10)
    node5 = Node(2, node3, node4)
    assert solution(node5)

    node9 = Node(9)
    node8 = Node(8, None, node9)
    node7 = Node(7)
    node6 = Node(6)
    node5 = Node(5)
    node4 = Node(4, node7, node8)
    node3 = Node(3, node5, node6)
    node2 = Node(2, None, node4)
    node1 = Node(1, node3, None)
    node0 = Node(0, node1, node2)

    assert not solution(node0)


if __name__ == '__main__':
    test()
