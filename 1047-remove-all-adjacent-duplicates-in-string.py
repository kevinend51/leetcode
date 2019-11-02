#!/usr/bin/env python3


class Solution:
    def removeDuplicates(self, S: str) -> str:
        l = []
        for c in S:
            if len(l) > 0 and l[-1] == c:
                l.pop()
            else:
                l.append(c)
        return ''.join(l)
