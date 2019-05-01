#!/usr/bin/env python3

import re


class Solution:
    regex = re.compile('(?P<name>[\w.]+)([+][\w.+]+)?@(?P<domain>[\w.]+)')

    def extract_tuple(self, email):
        match = self.regex.match(email)
        name = match.group('name').replace('.', '')
        domain = match.group('domain')
        return (name, domain)

    def numUniqueEmails(self, emails: List[str]) -> int:
        return len(set(map(self.extract_tuple, emails)))
