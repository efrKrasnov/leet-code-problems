from collections import deque

from main import Solution, TreeNode


def level_order_traverse(tree: TreeNode | None) -> list[list[int]]:
    result = []
    items: deque[TreeNode] = deque([])
    if not tree:
        return result
    items.append(tree)
    while items:
        vals_in_row = []
        items_count = len(items)
        for _ in range(items_count):
            item = items.popleft()
            vals_in_row.append(item.val)
            if item.left:
                items.append(item.left)
            if item.right:
                items.append(item.right)
        result.append(vals_in_row)
    return result


def test_1():
    preorder = [3, 9, 20, 15, 7]
    inorder = [9, 3, 15, 20, 7]
    
    s = Solution()
    tree = s.buildTree(preorder, inorder)
    assert level_order_traverse(tree) == [[3], [9, 20], [15, 7]]
    
    
def test_2():
    preorder = [-1]
    inorder = [-1]
    
    s = Solution()
    tree = s.buildTree(preorder, inorder)
    assert level_order_traverse(tree) == [[-1]]
    
    