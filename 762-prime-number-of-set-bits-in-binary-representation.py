#!/usr/bin/env python3


class Solution:
    prime_table = {0: False, 1: False}

    def is_prime(self, n):
        if n not in self.prime_table:
            self.prime_table[n] = True
            for i in range(2, n):
                if not n % i:
                    self.prime_table[n] = False
                    break
        return self.prime_table[n]

    def check(self, n):
        ones = bin(n)[2:].count('1')
        return self.is_prime(ones)

    def countPrimeSetBits(self, L: int, R: int) -> int:
        return sum(map(self.check, range(L, R + 1)))
