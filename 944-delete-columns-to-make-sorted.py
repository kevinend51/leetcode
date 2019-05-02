#!/usr/bin/env python3

from functools import reduce


class Solution:
    def decreasing(self, A):
        for i in range(len(A) - 1):
            if A[i] > A[i+1]:
                return True
        return False

    def minDeletionSize(self, A: List[str]) -> int:
        cols = zip(*A)
        cols = filter(self.decreasing, cols)
        return reduce(lambda acc, val: acc + 1, cols, 0)
