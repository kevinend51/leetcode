#!/usr/bin/env python3

"""
# Definition for a Node.
class Node:
    def __init__(self, val, children):
        self.val = val
        self.children = children
"""


class Solution:
    def maxDepth(self, root: 'Node') -> int:
        stack = []
        result = 0
        while root or stack:
            if root:
                stack.append({'root': root, 'idx': 0})
                root = None
                result = max(result, len(stack))
            else:
                ctx = stack[-1]
                if ctx['idx'] < len(ctx['root'].children):
                    root = ctx['root'].children[ctx['idx']]
                    ctx['idx'] += 1
                else:
                    stack.pop()
        return result
