from typing import Callable
from main import Solution, TreeNode


def level_order_traverse(tree: TreeNode | None, func: Callable[[int], None]):
    from collections import deque

    if not tree:
        return tree

    items: deque[TreeNode] = deque([])
    items.append(tree)

    while items:
        item = items.popleft()
        func(item.val)

        if item.left:
            items.append(item.left)
        if item.right:
            items.append(item.right)


def test_1():
    inorder = [9, 3, 15, 20, 7]
    postorder = [9, 15, 7, 20, 3]

    s = Solution()
    tree = s.buildTree(inorder, postorder)

    items: list[int] = []

    def push(val):
        items.append(val)

    level_order_traverse(tree, push)
    
    assert items == [3, 9, 20, 15, 7]


def test_2():
    inorder = [-1]
    postorder = [-1]

    s = Solution()
    tree = s.buildTree(inorder, postorder)

    items: list[int] = []

    def push(val):
        items.append(val)

    level_order_traverse(tree, push)
    
    assert items == [-1]


def test_3():
    inorder: list[int] = []
    postorder: list[int] = []

    s = Solution()
    tree = s.buildTree(inorder, postorder)

    assert tree is None
