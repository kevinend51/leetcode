#!/usr/bin/env python3


class Solution:
    table = {0: 0, 1: 1}

    def fib(self, N: int) -> int:
        if N not in self.table:
            self.table[N] = self.fib(N - 1) + self.fib(N - 2)
        return self.table[N]
