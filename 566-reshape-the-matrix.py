#!/usr/bin/env python3

from itertools import chain
from functools import reduce


class Solution:
    def matrixReshape(self, nums: List[List[int]], r: int, c: int) -> List[List[int]]:
        r0 = len(nums)
        c0 = len(nums[0])
        if r0 * c0 != r * c:
            return nums
        else:
            result = [[]]
            for num in reduce(chain, nums, []):
                if len(result[-1]) == c:
                    result.append([])
                result[-1].append(num)
            return result
