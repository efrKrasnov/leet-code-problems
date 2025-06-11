from dataclasses import dataclass
from typing import Self


@dataclass
class TreeNode:
    val: int = 0
    left: Self | None = None
    right: Self | None = None
    

class Solution:
    def isSymmetric(self, root: TreeNode | None) -> bool:
        if root:
            return self.is_mirror(root.left, root.right)
        return True
    
    def is_mirror(self, left: TreeNode | None, right: TreeNode | None) -> bool:
        if not left and not right:
            return True
        elif not left or not right:
            return False
        return left.val == right.val and self.is_mirror(left.left, right.right) and self.is_mirror(left.right, right.left)