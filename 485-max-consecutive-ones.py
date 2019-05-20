#!/usr/bin/env python3


class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        c, C = 0, 0
        for num in nums:
            if num == 1:
                c += 1
                C = max(C, c)
            else:
                c = 0
        return C
