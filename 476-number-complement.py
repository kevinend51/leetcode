#!/usr/bin/env python3


class Solution:
    def findComplement(self, num: int) -> int:
        S = map(lambda s: '1' if s == '0' else '0', bin(num)[2:])
        return int(''.join(S), 2)
