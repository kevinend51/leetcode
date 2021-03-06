#!/usr/bin/env python3

from collections import Counter
from functools import reduce


class Solution:
    def commonChars(self, A: List[str]) -> List[str]:
        counters = [Counter(a) for a in A]
        counter = reduce(lambda acc, val: acc & val, counters[1:], counters[0])
        return list(counter.elements())
