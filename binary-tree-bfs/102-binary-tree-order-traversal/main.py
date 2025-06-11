from dataclasses import dataclass
from typing import Self


@dataclass
class TreeNode:
    val: int = 0
    left: Self | None = None
    right: Self | None = None
    
    
class Solution:
    def levelOrder(self, root: TreeNode | None) -> list[list[int]]:
        from collections import deque
        
        result: list[list[int]] = []
        
        if not root:
            return result
        
        items: deque[TreeNode] = deque([])
        items.append(root)
        while items:
            items_on_level_count = len(items)
            vals_on_level = []
            for _ in range(items_on_level_count):
                item = items.popleft()
                vals_on_level.append(item.val)
                if item.left:
                    items.append(item.left)
                if item.right:
                    items.append(item.right)
                    
            result.append(vals_on_level)
        return result