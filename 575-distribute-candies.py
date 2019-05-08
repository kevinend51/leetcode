#!/usr/bin/env python3


class Solution:
    def distributeCandies(self, candies: List[int]) -> int:
        count = len(candies)
        kind = len(set(candies))
        return min(count // 2, kind)
