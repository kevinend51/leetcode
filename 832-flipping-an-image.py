#!/usr/bin/env python3


class Solution:
    def flipAndInvertImage(self, A: List[List[int]]) -> List[List[int]]:
        for l in A:
            l.reverse()
            for i, v in enumerate(l):
                l[i] = 1 if v == 0 else 0
        return A
