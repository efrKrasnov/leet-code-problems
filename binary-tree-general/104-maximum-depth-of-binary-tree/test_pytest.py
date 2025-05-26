from main import TreeNode, Solution


def test_1():
    root = TreeNode(
        3,
        TreeNode(9),
        TreeNode(
            20,
            TreeNode(15),
            TreeNode(7)
        )
    )
    s = Solution()
    assert s.maxDepth(root) == 3
    
    
def test_2():
    root = TreeNode(
        1,
        None,
        TreeNode(2)
    )
    s = Solution()
    assert s.maxDepth(root) == 2
    