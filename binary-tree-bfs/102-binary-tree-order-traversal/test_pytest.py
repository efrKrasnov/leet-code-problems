from main import TreeNode, Solution


def test_1():
    tree = TreeNode(
        3,
        TreeNode(
            9
        ),
        TreeNode(
            20,
            TreeNode(15),
            TreeNode(7)
        )
    )
    s = Solution()
    assert s.levelOrder(tree) == [[3], [9, 20], [15, 7]]
    
    
def test_2():
    tree = TreeNode(
        1,
    )
    s = Solution()
    assert s.levelOrder(tree) == [[1]]
    
    
def test_3():
    tree = None
    s = Solution()
    assert s.levelOrder(tree) == []
    
    
