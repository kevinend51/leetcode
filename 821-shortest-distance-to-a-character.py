#!/usr/bin/env python3


class Solution:
    def shortestToChar(self, S: str, C: str) -> List[int]:
        idx = []
        for i, s in enumerate(S):
            if s == C:
                idx.append(i)
        result = []
        for i in range(len(S)):
            result.append(min(abs(i - j) for j in idx))
        return result
