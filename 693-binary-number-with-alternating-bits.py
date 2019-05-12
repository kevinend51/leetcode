#!/usr/bin/env python3


class Solution:
    def hasAlternatingBits(self, n: int) -> bool:
        b = bin(n)[2:]
        last = None
        for d in b:
            if last and d == last:
                return False
            last = d
        return True
