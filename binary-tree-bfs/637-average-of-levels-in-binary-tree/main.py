from dataclasses import dataclass
from typing import Self


@dataclass
class TreeNode:
    val: int = 0
    left: Self | None = None
    right: Self | None = None
    
    
class Solution:
    def averageOfLevels(self, root: TreeNode | None = None) -> list[float]:
        result = []
        if root:
            items: list[TreeNode] = []
            items.insert(0, root)
            
            while items:
                items_count = len(items)
                temp_sum = 0
                for _ in range(items_count):
                    item = items.pop()
                    temp_sum += item.val
                    if item.left:
                        items.insert(0, item.left)
                    if item.right:
                        items.insert(0, item.right)
                        
                result.append(float(temp_sum) / items_count)
                
        return result