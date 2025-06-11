from dataclasses import dataclass
from typing import Self

@dataclass
class TreeNode:
    val: int
    left: Self | None = None
    right: Self | None = None
    
class Solution:
    def rightSideView(self, root: TreeNode | None) -> list[int]:
        from collections import deque
        
        result: list[int] = []
        
        if root:
            items: deque[TreeNode] = deque([])
            items.append(root)
            
            while items:
                result.append(items[-1].val)
                items_count = len(items)
                for _ in range(items_count):
                    item = items.popleft()
                    if item.left:
                        items.append(item.left)
                    if item.right:
                        items.append(item.right)
                    
            
        return result