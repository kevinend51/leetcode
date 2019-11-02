#!/usr/bin/env python3


class Solution:
    def minCostToMoveChips(self, chips: List[int]) -> int:
        odd = len(list(filter(lambda v: v % 2 == 1, chips)))
        even = len(chips) - odd
        return min(odd, even)
