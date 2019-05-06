#!/usr/bin/env python3


class Solution:
    def calPoints(self, ops: List[str]) -> int:
        result = 0
        stack = []
        for op in ops:
            if op == '+':
                stack.append(stack[-1] + stack[-2])
                result += stack[-1]
            elif op == 'D':
                stack.append(stack[-1] * 2)
                result += stack[-1]
            elif op == 'C':
                result -= stack[-1]
                stack.pop()
            else:
                stack.append(int(op))
                result += stack[-1]
        return result
