#!/usr/bin/env python3


class Solution:
    def sumEvenAfterQueries(self, A: List[int], queries: List[List[int]]) -> List[int]:
        result = []
        even_sum = sum(filter(lambda a: not a % 2, A))
        for q in queries:
            inc, idx = q
            old_even = not A[idx] % 2
            new_even = not (A[idx] + inc) % 2
            if old_even and new_even:
                even_sum += inc
            elif not old_even and new_even:
                even_sum += A[idx] + inc
            elif old_even and not new_even:
                even_sum -= A[idx]
            A[idx] += inc
            result.append(even_sum)
        return result
