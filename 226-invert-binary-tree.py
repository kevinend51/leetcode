#!/usr/bin/env python3

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None


class Solution:
    def invertTree(self, root: TreeNode) -> TreeNode:
        if not root:
            return None
        result = TreeNode(root.val)
        result.left = self.invertTree(root.right)
        result.right = self.invertTree(root.left)
        return result
