#!/usr/bin/env python3

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None


class Solution:
    def traverse(self, root):
        if not root:
            return
        if root.left:
            self.traverse(root.left)
        self.result.right = TreeNode(root.val)
        self.result = self.result.right
        if root.right:
            self.traverse(root.right)

    def increasingBST(self, root: TreeNode) -> TreeNode:
        result = self.result = TreeNode(None)
        self.traverse(root)
        return result.right
