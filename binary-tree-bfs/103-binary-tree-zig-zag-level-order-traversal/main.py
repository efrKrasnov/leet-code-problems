from typing import Self
from dataclasses import dataclass


@dataclass
class TreeNode:
    val: int = 0
    left: Self | None = None
    right: Self | None = None
    
    
class Solution:
    def zigzagLevelOrder(self, root: TreeNode | None = None) -> list[list[int]]:
        from collections import deque
        
        result: list[list[int]] = []
        items: deque[TreeNode] = deque([])
        
        is_zig = True
        
        if root:
            items.append(root)
            
        while items:
            items_count = len(items)
            items_buf = [0] * items_count
            
            for i in range(items_count):
                item = items.popleft()
                if is_zig:
                    items_buf[i] = item.val
                else:
                    items_buf[-i-1] = item.val
                    
                if item.left:
                    items.append(item.left)
                if item.right:
                    items.append(item.right)
                    
            is_zig = not is_zig  
            result.append(items_buf)
        
        return result
