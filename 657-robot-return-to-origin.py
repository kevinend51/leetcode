#!/usr/bin/env python3

from collections import Counter


class Solution:
    def judgeCircle(self, moves: str) -> bool:
        c = Counter(moves)
        return c['L'] == c['R'] and c['D'] == c['U']
