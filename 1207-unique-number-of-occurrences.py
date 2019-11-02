#!/usr/bin/env python3

from collections import Counter


class Solution:
    def uniqueOccurrences(self, arr: List[int]) -> bool:
        counter = Counter(arr)
        occurs = [counter[k] for k in counter]
        return len(occurs) == len(set(occurs))
