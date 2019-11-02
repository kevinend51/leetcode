#!/usr/bin/env python3


class Solution:
    def relativeSortArray(self, arr1: List[int], arr2: List[int]) -> List[int]:
        key = {v: i for i, v in enumerate(arr2)}
        max_key = max(arr2)
        key_fn = lambda v: key[v] if v in key else max_key + v
        return sorted(arr1, key=key_fn)
