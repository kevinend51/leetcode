#!/usr/bin/env python3

from itertools import product


class Solution:
    def allCellsDistOrder(self, R: int, C: int, r0: int, c0: int) -> List[List[int]]:
        coords = product(range(R), range(C))
        return sorted(coords, key=lambda c: abs(c[0] - r0) + abs(c[1] - c0))
