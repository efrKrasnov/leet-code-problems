from main import Node, Solution


def test_1():
    tree = Node(1, Node(2, Node(4), Node(5)), Node(3, None, Node(7)))
    s = Solution()
    s.connect(tree)
    assert tree.next is None

    tree_left = tree.left
    assert tree_left is not None
    assert tree_left.val == 2
    assert tree_left.next is not None
    assert tree_left.next.val == 3
    assert tree_left.next.next is None

    tree_left = tree_left.left
    assert tree_left is not None
    assert tree_left.val == 4
    assert tree_left.next is not None
    assert tree_left.next.val == 5
    assert tree_left.next.next is not None
    assert tree_left.next.next.val == 7
    assert tree_left.next.next.next is None


def test_2():
    tree = None
    s = Solution()
    s.connect(tree)
    assert tree is None
