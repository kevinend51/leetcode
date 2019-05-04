#!/usr/bin/env python3

from functools import reduce
from collections import Counter


class Solution:
    def count_cpdomain(self, cpdomain):
        cnt, domain = cpdomain.split()
        cnt = int(cnt)
        tokens = domain.split('.')[::-1]
        domains = ('.'.join(tokens[:i + 1][::-1]) for i in range(len(tokens)))
        return Counter({d: cnt for d in domains})

    def update_counter(self, c1, c2):
        c1.update(c2)
        return c1

    def subdomainVisits(self, cpdomains: List[str]) -> List[str]:
        counters = list(map(self.count_cpdomain, cpdomains))
        counter = reduce(self.update_counter, counters[1:], counters[0])
        return list(map(lambda i: '{} {}'.format(i[1], i[0]), counter.items()))
