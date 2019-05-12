#!/usr/bin/env python3


class Solution:
    def largestPerimeter(self, A: List[int]) -> int:
        A = sorted(A, reverse=True)
        for i in range(len(A) - 2):
            a0, a1, a2 = A[i:i + 3]
            if a1 + a2 > a0:
                return a0 + a1 + a2
        return 0
