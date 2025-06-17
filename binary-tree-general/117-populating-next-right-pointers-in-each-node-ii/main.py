from dataclasses import dataclass
from typing import Self


@dataclass
class Node:
    val: int = 0
    left: Self | None = None
    right: Self | None = None
    next: Self | None = None
    
    
class Solution:
    def connect(self, root: Node | None) -> Node | None:
        from collections import deque
        
        items: deque[Node] = deque([])
        
        if not root:
            return root
        
        items.append(root)
        while items:
            items_count = len(items)
            set_next_times = items_count - 1
            for _ in range(items_count):
                item = items.popleft()
                if item.left:
                    items.append(item.left)
                if item.right:
                    items.append(item.right)
                if set_next_times:
                    item.next = items[0]
                    set_next_times -= 1
                    
        return root