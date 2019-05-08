#!/usr/bin/env python3

from functools import reduce


class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        return reduce(lambda acc, val: acc ^ val, nums, 0)
