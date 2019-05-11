#!/usr/bin/env python3

from itertools import chain
from functools import cmp_to_key


class Solution:
    def is_letter(self, log):
        return ''.join(log.split()[1:]).isalpha()

    def cmp_letter(self, log1, log2):
        id1, letter1 = log1.split(' ', 1)
        id2, letter2 = log2.split(' ', 1)
        if letter1 < letter2:
            return -1
        elif letter1 == letter2:
            if id1 < id2:
                return -1
            elif id1 == id2:
                return 0
            else:
                return 1
        else:
            return 1

    def reorderLogFiles(self, logs: List[str]) -> List[str]:
        letter_logs = filter(self.is_letter, logs)
        digit_logs = filter(lambda l: not self.is_letter(l), logs)
        letter_logs = sorted(letter_logs, key=cmp_to_key(self.cmp_letter))
        return letter_logs + list(digit_logs)
