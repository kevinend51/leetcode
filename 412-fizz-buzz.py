#!/usr/bin/env python3


class Solution:
    def calc(self, v):
        if not v % 15:
            return 'FizzBuzz'
        elif not v % 3:
            return 'Fizz'
        elif not v % 5:
            return 'Buzz'
        else:
            return str(v)

    def fizzBuzz(self, n: int) -> List[str]:
        return list(map(self.calc, range(1, n + 1)))
