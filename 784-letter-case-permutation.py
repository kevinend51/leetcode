#!/usr/bin/env python3


class Solution:
    def letterCasePermutation(self, S: str) -> List[str]:
        def backtrack(i):
            nonlocal S
            if i == len(S):
                yield S
            elif not S[i].isalpha():
                yield from backtrack(i + 1)
            else:
                for s in S[i].lower(), S[i].upper():
                    S = S[:i] + s + S[i+1:]
                    yield from backtrack(i + 1)
        return list(backtrack(0))
