#!/usr/bin/env python3


class Solution:
    def removeOuterParentheses(self, S: str) -> str:
        result = ''
        count = 0
        for s in S:
            count += 1 if s == '(' else -1
            if s == '(' and count > 1 or s == ')' and count > 0:
                result += s
        return result
