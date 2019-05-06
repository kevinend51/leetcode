#!/usr/bin/env python3

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None


class Solution:
    def get_leaf(self, root, result=None):
        if result is None:
            result = []
        if root and not (root.left or root.right):
            result.append(root.val)
        elif root and (root.left or root.right):
            self.get_leaf(root.left, result)
            self.get_leaf(root.right, result)
        return result

    def leafSimilar(self, root1: TreeNode, root2: TreeNode) -> bool:
        return self.get_leaf(root1) == self.get_leaf(root2)
