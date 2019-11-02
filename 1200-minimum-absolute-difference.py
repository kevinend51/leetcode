#!/usr/bin/env python3


class Solution:
    def minimumAbsDifference(self, arr: List[int]) -> List[List[int]]:
        arr = sorted(arr)
        diff = min(arr[i+1] - arr[i] for i in range(len(arr) - 1))
        return list(filter(
            lambda pair: pair[1] - pair[0] == diff,
            ([arr[i], arr[i+1]] for i in range(len(arr) - 1))
        ))
