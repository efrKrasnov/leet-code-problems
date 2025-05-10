from main import Solution, ListNode


def test_1():
    head = ListNode(3)
    pos = ListNode(2)
    cycle_items = ListNode(0, ListNode(-4, pos))
    head.next = pos
    pos.next = cycle_items

    s = Solution()
    assert s.detectCycle(head) == pos


def test_2():
    head = ListNode(1)
    pos = ListNode(2)
    head.next = pos
    pos.next = head

    s = Solution()
    assert s.detectCycle(head) == head


def test_3():
    head = ListNode(1)

    s = Solution()
    assert s.detectCycle(head) is None
