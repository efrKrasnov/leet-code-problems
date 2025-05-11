class ListNode:
    def __init__(self, val=0, next=None):
        self.val: int = val
        self.next: None | ListNode = next
        
class List:
    def __init__(self) -> None:
        self.head: ListNode | None = None
    
    def insert(self, val) -> None:
        node = ListNode(val)
        node.next = self.head
        self.head = node
        
    def pop(self) -> int | None:
        node: ListNode | None = self.head
        if not node:
            return None
        else:
            self.head = node.next
            return node.val
    
class Solution:
    def addTwoNumbers(self, l1: ListNode | None, l2: ListNode | None) -> ListNode | None:
        head: ListNode = ListNode()
        tail: ListNode = head
        tail_prev = None
        carry = 0
        while l1 or l2:
            # Вычисляем сумму с переносом
            v1 = l1.val if l1 else 0
            v2 = l2.val if l2 else 0
            t_sum = v1 + v2 + carry
            carry = 0
            if t_sum >= 10:
                carry = 1
                t_sum = t_sum - 10
            
            # Выполняем вставку
            tail.val = t_sum
            tail.next = ListNode()
            tail_prev = tail
            tail = tail.next
            if l1:
                l1 = l1.next
            if l2:
                l2 = l2.next
        
        # Отслеживаем перенос
        if carry:
            tail.val = carry
        else:
            if tail_prev:
                tail_prev.next = None
            
        return head
            