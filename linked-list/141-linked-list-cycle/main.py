class ListNode:
    def __init__(self, x, next=None):
        self.val = x
        self.next = next

class Solution:
    def hasCycle(self, head: ListNode | None) -> bool:
        is_have_cycle = False
        hare_ptr = head
        tortoise_ptr = head
        
        while hare_ptr and tortoise_ptr:
            hare_ptr = self.move_forward(hare_ptr, 2)
            tortoise_ptr = self.move_forward(tortoise_ptr, 1)
            if hare_ptr and tortoise_ptr and (hare_ptr == tortoise_ptr):
                is_have_cycle = True
                break
            
        return is_have_cycle
            
            
    def move_forward(self, node: ListNode | None, count: int = 1):
        while count:
            if node:
                node = node.next
            else:
                break
            count -= 1
        return node
            