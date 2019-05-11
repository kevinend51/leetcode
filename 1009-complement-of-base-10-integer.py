#!/usr/bin/env python3


class Solution:
    def bitwiseComplement(self, N: int) -> int:
        b = bin(N)[2:]
        b = ''.join(map(lambda d: '1' if d == '0' else '0', b))
        return int(b, 2)
