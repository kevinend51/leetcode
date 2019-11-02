#!/usr/bin/env python3


class Solution:
    def balancedStringSplit(self, s: str) -> int:
        result, count = 0, 0
        for c in s:
            count += 1 if c == 'R' else -1
            if count == 0:
                result += 1
        return result
