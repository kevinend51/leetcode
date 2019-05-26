#!/usr/bin/env python3

from functools import reduce


class Solution:
    table = {'0': '0', '1': '1', '8': '8', '2': '5', '5': '2', '6': '9', '9': '6'}

    def is_valid(self, num):
        return (set(str(num)).issubset(self.table.keys()) and
                int(''.join(self.table[c] for c in str(num))) != num)

    def rotatedDigits(self, N: int) -> int:
        nums = filter(self.is_valid, range(1, N + 1))
        return reduce(lambda acc, val: acc + 1, nums, 0)
