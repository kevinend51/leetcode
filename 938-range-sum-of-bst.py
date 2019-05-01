#!/usr/bin/env python3

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None


class Solution:
    def rangeSumBST(self, root: TreeNode, L: int, R: int) -> int:
        if root is None:
            return 0

        result = root.val if L <= root.val <= R else 0
        if L < root.val:
            result += self.rangeSumBST(root.left, L, R)
        if root.val < R:
            result += self.rangeSumBST(root.right, L, R)
        return result
