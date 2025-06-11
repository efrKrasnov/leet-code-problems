from dataclasses import dataclass
from typing import Self


@dataclass
class TreeNode:
    val: int
    left: Self | None = None
    right: Self | None = None
    
    
class Solution:
    def buildTree(self, preorder: list[int], inorder: list[int]) -> TreeNode | None:
        if not preorder and not inorder:
            return None
        
        if len(preorder) == 1:
            return TreeNode(preorder[0])
        
        val = preorder[0]
        val_pos = inorder.index(val)
        
        tree = TreeNode(val)
        tree.left = self.buildTree(preorder[1:val_pos + 1], inorder[:val_pos]) 
        tree.right = self.buildTree(preorder[val_pos + 1: ], inorder[val_pos+1:]) 
        
        return tree
        