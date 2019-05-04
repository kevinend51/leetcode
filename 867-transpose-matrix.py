#!/usr/bin/env python3


class Solution:
    def transpose(self, A: List[List[int]]) -> List[List[int]]:
        rows = len(A)
        cols = len(A[0])
        result = [[None for _ in range(rows)] for _ in range(cols)]
        for r in range(rows):
            for c in range(cols):
                result[c][r] = A[r][c]
        return result
