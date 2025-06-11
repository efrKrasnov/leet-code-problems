from main import Solution, TreeNode


def test_1():
    tree = TreeNode(
        1,
        TreeNode(
            2,
            TreeNode(3),
            TreeNode(4)
        ),
        TreeNode(
            2,
            TreeNode(4),
            TreeNode(3)
        )
    )
    s = Solution()
    assert s.isSymmetric(tree) is True
    
    
def test_2():
    tree = TreeNode(
        1,
        TreeNode(
            2,
            None,
            TreeNode(3)
        ),
        TreeNode(
            2,
            None,
            TreeNode(3)
        )
    )
    s = Solution()
    assert s.isSymmetric(tree) is False