from main import Solution, TreeNode


def test_1():
    tree = TreeNode(
        3, 
        TreeNode(9),
        TreeNode(
            20,
            TreeNode(15),
            TreeNode(7)
        )
    )
    s = Solution()
    assert s.averageOfLevels(tree) == [3 / 1, (9 + 20) / 2, (15 + 7) / 2]
    
    
def test_2():
    tree = TreeNode(
        3, 
        TreeNode(
            9,
            TreeNode(15),
            TreeNode(7)
        ),
        TreeNode(20)
    )
    s = Solution()
    assert s.averageOfLevels(tree) == [3 / 1, (9 + 20) / 2, (15 + 7) / 2]