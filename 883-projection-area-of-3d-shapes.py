#!/usr/bin/env python

from itertools import chain


class Solution:
    def projectionArea(self, grid: List[List[int]]) -> int:
        xz = sum(map(max, grid))
        yz = sum(map(max, zip(*grid)))
        xy = sum(map(lambda v: min(1, v), chain(*grid)))
        return xz + yz + xy
