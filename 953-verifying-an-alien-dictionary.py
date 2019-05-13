#!/usr/bin/env python3


class Solution:
    def isAlienSorted(self, words: List[str], order: str) -> bool:
        table = dict(zip(order, 'abcdefghijklmnopqrstuvwxyz'))
        return words == sorted(words, key=lambda w: ''.join(table[c] for c in w))
