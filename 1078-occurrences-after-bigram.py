#!/usr/bin/env python3


class Solution:
    def findOcurrences(self, text: str, first: str, second: str) -> List[str]:
        tokens = text.split()
        result = []
        for i in range(len(tokens) - 2):
            if tokens[i] == first and tokens[i+1] == second:
                result.append(tokens[i+2])
        return result
