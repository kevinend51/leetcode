#!/usr/bin/env python3

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None


class Solution:
    def isUnivalTree(self, root: TreeNode) -> bool:
        if not root:
            return True
        elif root.right and root.val != root.right.val:
            return False
        elif root.left and root.val != root.left.val:
            return False
        else:
            return self.isUnivalTree(root.left) and self.isUnivalTree(root.right)
