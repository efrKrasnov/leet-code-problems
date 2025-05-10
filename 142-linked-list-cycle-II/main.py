from typing import Self

class ListNode:
    def __init__(self, x, next: Self | None = None):
        self.val = x
        self.next = next


class Solution:
    def detectCycle(self, head: ListNode | None) -> ListNode | None:
        h_ptr = head
        t_ptr = head
        is_cycle_exists = False
        
        # step 1 detect cycle
        while h_ptr and t_ptr:
            h_ptr = self.move(h_ptr, 2)
            t_ptr = self.move(t_ptr)
            
            if h_ptr and t_ptr and (h_ptr == t_ptr):
                is_cycle_exists = True
                break
        
        # step 2 detect item      
        if is_cycle_exists:
            h_ptr = head
            while h_ptr != t_ptr:
                h_ptr = self.move(h_ptr)
                t_ptr = self.move(t_ptr)
            return h_ptr
        else:
            return None
        
    def move(self, node: ListNode | None, count: int = 1) -> ListNode | None:
        for i in range(count):
            if node:
                node = node.next
            else:
                break
            
        return node