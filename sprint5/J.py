import os

LOCAL = os.environ.get('REMOTE_JUDGE', 'false') != 'true'

if not LOCAL:
    from node import Node

if LOCAL:
    class Node:
        def __init__(self, left=None, right=None, value=0):
            self.right = right
            self.left = left
            self.value = value


def insert(root, key):
    if root is None:
        return Node(value=key)

    current = root
    while current:
        if key < current.value:
            if current.left is None:
                current.left = Node(value=key)
                break

            current = current.left
        else:
            if current.right is None:
                current.right = Node(value=key)
                break

            current = current.right

    return root


def test():
    node1 = Node(None, None, 7)
    node2 = Node(node1, None, 8)
    node3 = Node(None, node2, 7)
    new_head = insert(node3, 6)
    assert new_head is node3
    assert new_head.left.value == 6


if __name__ == '__main__':
    test()