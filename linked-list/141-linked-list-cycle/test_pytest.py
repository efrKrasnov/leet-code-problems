from main import Solution, ListNode


def test_1():
    s = Solution()
    head = ListNode(3)
    pos = ListNode(2)
    cycle_items = ListNode(0, ListNode(-4, pos))
    pos.next = cycle_items
    head.next = pos
    assert s.hasCycle(head) is True
    
    
def test_2():
    s = Solution()
    head = ListNode(1)
    pos = ListNode(2)
    pos.next = head
    head.next = pos
    assert s.hasCycle(head) is True
    
    
def test_3():
    s = Solution()
    head = ListNode(1)
    assert s.hasCycle(head) is False