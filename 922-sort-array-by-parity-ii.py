#!/usr/bin/env python3

from functools import reduce


class Solution:
    def extend(self, l1, l2):
        l1.extend(l2)
        return l1

    def sortArrayByParityII(self, A: List[int]) -> List[int]:
        pairs = zip(filter(lambda a: not a%2, A), filter(lambda a: a%2, A))
        return reduce(lambda acc, val: self.extend(acc, val), pairs, [])
