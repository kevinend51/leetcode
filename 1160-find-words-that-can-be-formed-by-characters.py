#!/usr/bin/env python3

from collections import Counter


class Solution:
    def is_good(self, word, chars):
        w_counter = Counter(word)
        c_counter = Counter(chars)
        for c in w_counter:
            if w_counter[c] > c_counter[c]:
                return False
        return True

    def countCharacters(self, words: List[str], chars: str) -> int:
        result = 0
        for word in words:
            if self.is_good(word, chars):
                result += len(word)
        return result
