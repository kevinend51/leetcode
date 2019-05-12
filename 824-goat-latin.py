#!/usr/bin/env python3


class Solution:
    def convert(self, w, i):
        if w[0].lower() not in 'aeiou':
            w = w[1:] + w[0]
        return w + 'ma' + 'a' * i

    def toGoatLatin(self, S: str) -> str:
        words = (self.convert(w, i + 1) for i, w in enumerate(S.split()))
        return ' '.join(words)
