#!/usr/bin/env python3

from collections import Counter


class Solution:
    def uncommonFromSentences(self, A: str, B: str) -> List[str]:
        c = Counter(A.split())
        c.update(Counter(B.split()))
        return list(val for val, cnt in c.items() if cnt == 1)
