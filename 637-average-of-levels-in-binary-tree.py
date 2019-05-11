#!/usr/bin/env python3

from collections import deque

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None


class Solution:
    def averageOfLevels(self, root: TreeNode) -> List[float]:
        levels = []
        queue = deque()
        if root:
            queue.append([root, 0])
        while queue:
            node, level = queue.popleft()
            if level >= len(levels):
                levels.append([])
            levels[level].append(node.val)
            for child in filter(lambda v: v, [node.right, node.left]):
                queue.append([child, level + 1])
        return [sum(level) / len(level) for level in levels]
