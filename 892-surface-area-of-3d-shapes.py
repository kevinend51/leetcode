#!/usr/bin/env python3


class Solution:
    def surfaceArea(self, grid: List[List[int]]) -> int:
        result = 0
        for i, row in enumerate(grid):
            for j, val in enumerate(row):
                if val == 0:
                    continue
                result += (
                    2 +
                    max(0, val - (row[j - 1] if j != 0 else 0)) +
                    max(0, val - (row[j + 1] if j != len(row) - 1 else 0)) +
                    max(0, val - (grid[i - 1][j] if i != 0 else 0)) +
                    max(0, val - (grid[i + 1][j] if i != len(grid) - 1 else 0))
                )
        return result
