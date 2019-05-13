#!/usr/bin/env python3


class Solution:
    def reverseOnlyLetters(self, S: str) -> str:
        S, i, j = list(S), 0, len(S) - 1
        while True:
            while i < len(S) and not S[i].isalpha():
                i += 1
            while j >= 0 and not S[j].isalpha():
                j -= 1
            if i >= j:
                break
            S[i], S[j] = S[j], S[i]
            i, j = i + 1, j - 1
        return ''.join(S)
