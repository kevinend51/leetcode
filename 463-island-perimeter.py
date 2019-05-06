#!/usr/bin/env python3


class Solution:
    def islandPerimeter(self, grid: List[List[int]]) -> int:
        result = 0
        for i, row in enumerate(grid):
            for j, val in enumerate(row):
                if val == 1:
                    if i == 0 or grid[i - 1][j] == 0:
                        result += 1
                    if i == len(grid) - 1 or grid[i + 1][j] == 0:
                        result += 1
                    if j == 0 or grid[i][j - 1] == 0:
                        result += 1
                    if j == len(row) - 1 or grid[i][j + 1] == 0:
                        result += 1
        return result
