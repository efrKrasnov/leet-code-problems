from main import List, Solution


def test_1():
    l1 = List()
    l1.insert(3)
    l1.insert(4)
    l1.insert(2)
    
    l2 = List()
    l2.insert(4)
    l2.insert(6)
    l2.insert(5)
    
    l3 = List()
    s = Solution()
    l3.head = s.addTwoNumbers(l1.head, l2.head)
    assert l3.pop() == 7
    assert l3.pop() == 0
    assert l3.pop() == 8
    
    
def test_2():
    l1 = List()
    l1.insert(0)
    
    l2 = List()
    l2.insert(0)
    
    l3 = List()
    s = Solution()
    l3.head = s.addTwoNumbers(l1.head, l2.head)
    assert l3.pop() == 0
    
    
def test_3():
    l1 = List()
    l1.insert(9)
    l1.insert(9)
    l1.insert(9)
    l1.insert(9)
    l1.insert(9)
    l1.insert(9)
    l1.insert(9)
    
    l2 = List()
    l2.insert(9)
    l2.insert(9)
    l2.insert(9)
    l2.insert(9)
    
    l3 = List()
    s = Solution()
    l3.head = s.addTwoNumbers(l1.head, l2.head)
    assert l3.pop() == 8
    assert l3.pop() == 9
    assert l3.pop() == 9
    assert l3.pop() == 9
    assert l3.pop() == 0
    assert l3.pop() == 0
    assert l3.pop() == 0
    assert l3.pop() == 1
    