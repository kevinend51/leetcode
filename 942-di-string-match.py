#!/usr/bin/env python3


class Solution:
    def diStringMatch(self, S: str) -> List[int]:
        result = []
        m, M = 0, len(S)
        for s in S:
            if s == 'I':
                result.append(m)
                m += 1
            else:
                result.append(M)
                M -= 1
        result.append(m)
        return result
