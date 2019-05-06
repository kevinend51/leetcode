#!/usr/bin/env python3

from itertools import chain


class Solution:
    def not_toeplitz(self, r, c, matrix):
        v = None
        while r < len(matrix) and c < len(matrix[0]):
            if v is None:
                v = matrix[r][c]
            elif v != matrix[r][c]:
                return True
            r, c = r + 1, c + 1

    def isToeplitzMatrix(self, matrix: List[List[int]]) -> bool:
        R, C = len(matrix), len(matrix[0])
        for r, c in chain(((r, 0) for r in range(R)),
                          ((0, c) for c in range(C))):
            if self.not_toeplitz(r, c, matrix):
                return False
        return True
