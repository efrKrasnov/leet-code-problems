from dataclasses import dataclass
from typing import Self


@dataclass
class TreeNode:
    val: int = 0
    left: Self | None = None
    right: Self | None = None


class Solution:
    def buildTree(self, inorder: list[int], postorder: list[int]) -> TreeNode | None:
        mapping = {val: i for i, val in enumerate(inorder)}

        def build(low: int, high: int) -> TreeNode | None:
            if low > high:
                return None

            item = TreeNode(postorder.pop())
            mid = mapping[item.val]

            item.right = build(mid + 1, high)
            item.left = build(low, mid - 1)

            return item

        return build(0, len(inorder) - 1)
