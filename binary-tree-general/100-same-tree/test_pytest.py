from main import TreeNode, Solution


def test_1():
    p = TreeNode(
        1,
        TreeNode(2),
        TreeNode(3)
    )
    q = TreeNode(
        1,
        TreeNode(2),
        TreeNode(3)
    )
    s = Solution()
    assert s.isSameTree(p, q) is True
    
    
def test_2():
    p = TreeNode(
        1,
        TreeNode(2)
    )
    q = TreeNode(
        1,
        None,
        TreeNode(2)
    )
    s = Solution()
    assert s.isSameTree(p, q) is False
    
    
def test_3():
    p = TreeNode(
        1,
        TreeNode(2),
        TreeNode(1)
    )
    q = TreeNode(
        1,
        TreeNode(1),
        TreeNode(2)
    )
    s = Solution()
    assert s.isSameTree(p, q) is False
    
    