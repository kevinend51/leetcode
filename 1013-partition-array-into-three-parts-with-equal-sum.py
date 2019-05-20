#!/usr/bin/env python3


class Solution:
    def canThreePartsEqualSum(self, A: List[int]) -> bool:
        S = sum(A)
        if S % 3 != 0:
            return False
        s, c = 0, 0
        for a in A:
            s += a
            if s == S // 3:
                s, c = 0, c + 1
        return c >= 3
