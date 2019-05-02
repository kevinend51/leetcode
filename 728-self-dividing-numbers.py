#!/usr/bin/env python3


class Solution:
    def test(self, v):
        w = v
        while w:
            d = w % 10
            if d == 0 or (v % d != 0):
                return False
            w //= 10
        return True

    def selfDividingNumbers(self, left: int, right: int) -> List[int]:
        return list(filter(self.test, range(left, right + 1)))
