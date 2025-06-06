from typing import Callable
from main import Solution, TreeNode


def in_order_traverse(node: TreeNode | None, func: Callable[[int], None]):
    # Прямой обход дерева для тестов
    if node:
        func(node.val)
        in_order_traverse(node.left, func)
        in_order_traverse(node.right, func)
    
    
def test_1():
    tree = TreeNode(
        4,
        TreeNode(
            2,
            TreeNode(1),
            TreeNode(3)
        ),
        TreeNode(
            7,
            TreeNode(6),
            TreeNode(9)
        )
    )
    s = Solution()
    tree_inverted = s.invertTree(tree)
    
    items = []
    in_order_traverse(tree_inverted, lambda x: items.append(x)) 
    assert items == [4, 7, 9, 6, 2, 3, 1]
    
    
def test_2():
    tree = TreeNode(
        2,
        TreeNode(1),
        TreeNode(3)
    )
    s = Solution()
    tree_inverted = s.invertTree(tree)
    
    items = []
    in_order_traverse(tree_inverted, lambda x: items.append(x)) 
    assert items == [2, 3, 1]
    
    
def test_3():
    tree = None
    s = Solution()
    tree_inverted = s.invertTree(tree)
    
    items = []
    in_order_traverse(tree_inverted, lambda x: items.append(x)) 
    assert items == []