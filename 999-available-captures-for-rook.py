#!/usr/bin/env python3

from itertools import product


class Solution:
    def get_r_index(self, board):
        for i, row in enumerate(board):
            for j, val in enumerate(row):
                if val == 'R':
                    return i, j

    def check(self, coords, board):
        for i, j in coords:
            if board[i][j] == 'p':
                return 1
            if board[i][j] != '.':
                return 0
        return 0

    def numRookCaptures(self, board: List[List[str]]) -> int:
        ri, rj = self.get_r_index(board)
        products = [
            product([ri], range(rj - 1, -1, -1)),
            product([ri], range(rj + 1, len(board))),
            product(range(ri - 1, -1, -1), [rj]),
            product(range(ri + 1, len(board[0])), [rj])
        ]
        return sum(self.check(p, board) for p in products)
