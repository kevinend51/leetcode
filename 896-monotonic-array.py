#!/usr/bin/env python3

from functools import reduce


class Solution:
    def isMonotonic(self, A: List[int]) -> bool:
        D = [A[i] - A[i-1]for i in range(1, len(A))]
        return all(map(lambda v: v >= 0, D)) or all(map(lambda v: v <= 0, D))
