#!/usr/bin/env python3


class Solution:
    def findNext(self, n, nums, table):
        for i in range(table[n] + 1, len(nums)):
            if nums[i] > n:
                return nums[i]
        return -1

    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        table = {n: i for i, n in enumerate(nums2)}
        return [self.findNext(n, nums2, table) for n in nums1]
