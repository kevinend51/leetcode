#!/usr/bin/env python3

from functools import reduce


class Solution:
    def numJewelsInStones(self, J: str, S: str) -> int:
        iter = filter(lambda s: s in J, S)
        return reduce(lambda acc, val: acc + 1, iter, 0)
