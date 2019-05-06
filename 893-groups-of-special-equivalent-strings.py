#!/usr/bin/env python3

from collections import Counter


class Solution:
    def numSpecialEquivGroups(self, A: List[str]) -> int:
        A = [(tuple(sorted(a[::2])), tuple(sorted(a[1::2]))) for a in A]
        return len(Counter(A))
