"""
https://contest.yandex.ru/contest/24810/run-report/115373718/

Реализация метода удаления узла из бинарного дерева поиска.

При удалении узла из дерева необходимо учитывать три случая:
  1. У удаляемого узла нет детей (в этом случае удаляемый узел удаляется, а у родителя удаляемого узла обнуляется ссылка на удаляемый узел)
  2. У удаляемого узла есть только один ребенок (в этом случае удаляемый узел заменяется на своего ребенка)
  3. У удаляемого узла есть оба ребенка (в этом случае удаляемый узел заменяется на минимальный лист в правом поддереве, а лист удаляется)

Сложность по времени: O(h), где h - высота дерева
Сложность по памяти: O(1), так как операция производится без использования дополнительной памяти
"""

import os

LOCAL = os.environ.get('REMOTE_JUDGE', 'false') != 'true'

if LOCAL:
    class Node:
        def __init__(self, left=None, right=None, value=0):
            self.right = right
            self.left = left
            self.value = value
else:
    from node import Node


def remove(root, key):
    if root is None:
        return root

    node_search = find_node(root, key)
    if node_search is None:
        return root

    parent, node = node_search
    if node.left is None and node.right is None:
        # No children
        if parent is None:
            return None

        if parent.left is node:
            parent.left = None
        else:
            parent.right = None
    elif node.left is None:
        # Only right child
        if parent is None:
            return node.right

        if parent.left is node:
            parent.left = node.right
        else:
            parent.right = node.right
    elif node.right is None:
        # Only left child
        if parent is None:
            return node.left

        if parent.left is node:
            parent.left = node.left
        else:
            parent.right = node.left
    else:
        # Both children
        replace_leaf_parent, replace_leaf_node = find_min_leaf(node.right)
        node.value = replace_leaf_node.value

        if replace_leaf_parent is None:
            node.right = None
        else:
            replace_leaf_parent.left = None

    return root


def find_node(root, key):
    current = root
    parent = None
    while current:
        if key == current.value:
            return parent, current
        elif key < current.value:
            parent = current
            current = current.left
        else:
            parent = current
            current = current.right
    return None


def find_min_leaf(root):
    current = root
    parent = None
    while current.left is not None:
        parent = current
        current = current.left

    return parent, current


def test():
    node1 = Node(None, None, 2)
    node2 = Node(node1, None, 3)
    node3 = Node(None, node2, 1)
    node4 = Node(None, None, 6)
    node5 = Node(node4, None, 8)
    node6 = Node(node5, None, 10)
    node7 = Node(node3, node6, 5)
    newHead = remove(node7, 10)
    assert newHead.value == 5
    assert newHead.right is node5
    assert newHead.right.value == 8

    # Node to be removed has only right child
    node1 = Node(None, None, 2)
    node2 = Node(None, node1, 1)
    newHead = remove(node2, 1)
    assert newHead.value == 2
    assert newHead.left is None
    assert newHead.right is None

    # Node to be removed has both children
    node1 = Node(None, None, 2)
    node2 = Node(None, None, 4)
    node3 = Node(node1, node2, 3)
    newHead = remove(node3, 3)
    assert newHead.value == 4
    assert newHead.left is node1
    assert newHead.right is None

    # Node to be removed is the root
    node1 = Node(None, None, 2)
    node2 = Node(None, None, 4)
    node3 = Node(node1, node2, 3)
    newHead = remove(node3, 3)
    assert newHead.value == 4
    assert newHead.left is node1
    assert newHead.right is None


if __name__ == '__main__':
    test()
