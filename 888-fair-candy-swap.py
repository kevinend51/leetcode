#!/usr/bin/env python3


class Solution:
    def fairCandySwap(self, A: List[int], B: List[int]) -> List[int]:
        diff = (sum(B) - sum(A)) // 2
        SB = set(B)
        for a in A:
            if a + diff in SB:
                return [a, a + diff]
