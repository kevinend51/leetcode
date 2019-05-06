#!/usr/bin/env python3


class Solution:
    def numberOfLines(self, widths: List[int], S: str) -> List[int]:
        line, pos = 1, 0
        for s in S:
            w = widths[ord(s) - ord('a')]
            if pos + w > 100:
                line, pos = line + 1, 0
            pos += w
        return [line, pos]
