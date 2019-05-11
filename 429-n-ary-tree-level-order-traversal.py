#!/usr/bin/env python3

from collections import deque

"""
# Definition for a Node.
class Node:
    def __init__(self, val, children):
        self.val = val
        self.children = children
"""


class Solution:
    def levelOrder(self, root: 'Node') -> List[List[int]]:
        result = []
        queue = deque()
        if root:
            queue.append([root, 0])
        while queue:
            node, level = queue.popleft()
            if level >= len(result):
                result.append([])
            result[level].append(node.val)
            for child in node.children:
                queue.append([child, level + 1])
        return result
