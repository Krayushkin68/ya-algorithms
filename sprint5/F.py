import os

LOCAL = os.environ.get('REMOTE_JUDGE', 'false') != 'true'

if LOCAL:
    class Node:
        def __init__(self, value, left=None, right=None):
            self.value = value
            self.right = right
            self.left = left


def solution(root) -> int:
    if not root:
        return 0

    max_len = [1]
    dfs(root, 1, max_len)

    return max_len[0]


def dfs(node: 'Node', current_path_len: int, max_path_len: list[int]):
    if not node:
        return

    if not node.left and not node.right:
        max_path_len[0] = max(current_path_len, max_path_len[0])

    if node.left:
        dfs(node.left, current_path_len + 1, max_path_len)

    if node.right:
        dfs(node.right, current_path_len + 1, max_path_len)


def test():
    node1 = Node(1, None, None)
    node2 = Node(4, None, None)
    node3 = Node(3, node1, node2)
    node4 = Node(8, None, None)
    node5 = Node(5, node3, node4)

    assert solution(node5) == 3


if __name__ == '__main__':
    test()
