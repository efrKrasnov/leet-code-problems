from main import Solution, TreeNode

def test_1():
    tree = TreeNode(
        1,
        TreeNode(
            2,
            None,
            TreeNode(5)
        ),
        TreeNode(
            3,
            None,
            TreeNode(4)
        )
    )
    s = Solution()
    assert s.rightSideView(tree) == [1, 3, 4]
    
    
def test_2():
    tree = TreeNode(
        1,
        TreeNode(
            2,
            TreeNode(
                4,
                TreeNode(5),
                None
            ),
            None
        ),
        TreeNode(3)
    )
    s = Solution()
    assert s.rightSideView(tree) == [1, 3, 4, 5]
    
    
def test_3():
    tree = TreeNode(
        1,
        None,
        TreeNode(3)
    )
    s = Solution()
    assert s.rightSideView(tree) == [1, 3]
    
    
def test_4():
    tree = None
    s = Solution()
    assert s.rightSideView(tree) == []