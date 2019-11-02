#!/usr/bin/env python3


class Solution:
    def heightChecker(self, heights: List[int]) -> int:
        return sum([1 if i != j else 0 for (i, j) in zip(heights, sorted(heights))])
