#!/usr/bin/env python3

from itertools import product

"""
# Definition for a QuadTree node.
class Node:
    def __init__(self, val, isLeaf, topLeft, topRight, bottomLeft, bottomRight):
        self.val = val
        self.isLeaf = isLeaf
        self.topLeft = topLeft
        self.topRight = topRight
        self.bottomLeft = bottomLeft
        self.bottomRight = bottomRight
"""


class Solution:
    def check_leaf(self, grid, r0, c0, r1, c1):
        v = None
        for r, c in product(range(r0, r1), range(c0, c1)):
            if v is not None and v != grid[r][c]:
                return False
            v = grid[r][c]
        return True

    def split(self, grid, r0, c0, r1, c1):
        if self.check_leaf(grid, r0, c0, r1, c1):
            return Node(grid[r0][c0], True, None, None, None, None)
        else:
            rm, cm = (r0 + r1) // 2, (c0 + c1) // 2
            return Node(None, False,
                        self.split(grid, r0, c0, rm, cm),
                        self.split(grid, r0, cm, rm, c1),
                        self.split(grid, rm, c0, r1, cm),
                        self.split(grid, rm, cm, r1, c1))

    def construct(self, grid: List[List[int]]) -> 'Node':
        N = len(grid)
        return self.split(grid, 0, 0, N, N)
