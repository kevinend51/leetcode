#!/usr/bin/env python3

import heapq


class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        stones = list(map(lambda v: -v, stones))
        heapq.heapify(stones)
        while len(stones) > 1:
            s1 = heapq.heappop(stones)
            s2 = heapq.heappop(stones)
            if s1 > s2:
                heapq.heappush(stones, s2 - s1)
            elif s1 < s2:
                heapq.heappush(stones, s1 - s2)
        return -stones[0] if len(stones) > 0 else 0
