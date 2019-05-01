#!/usr/bin/env python3


class Solution:
    def sortedSquares(self, A: List[int]) -> List[int]:
        return sorted(a * a for a in A)
