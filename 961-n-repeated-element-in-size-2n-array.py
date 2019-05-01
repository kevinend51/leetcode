#!/usr/bin/env python3

from collections import defaultdict


class Solution:
    def repeatedNTimes(self, A: List[int]) -> int:
        count = defaultdict(int)
        for a in A:
            count[a] += 1
            if count[a] > 1:
                return a
