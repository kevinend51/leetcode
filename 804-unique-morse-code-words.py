#!/usr/bin/env python3


class Solution:
    table = [".-","-...","-.-.","-..",".","..-.","--.","....","..",".---","-.-",".-..","--","-.","---",".--.","--.-",".-.","...","-","..-","...-",".--","-..-","-.--","--.."]

    def encode_c(self, c):
        return self.table[ord(c) - ord('a')]

    def encode(self, word):
        return ''.join(map(self.encode_c, word))

    def uniqueMorseRepresentations(self, words: List[str]) -> int:
        results = set(map(self.encode, words))
        return len(results)
