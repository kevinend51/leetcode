#!/usr/bin/env python3


class Solution:
    rows = list(map(set, ['qwertyuiop', 'asdfghjkl', 'zxcvbnm']))

    def check(self, word):
        s = set(word.lower())
        for row in self.rows:
            if s <= row:
                return True

    def findWords(self, words):
        return list(filter(self.check, words))
