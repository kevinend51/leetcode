#!/usr/bin/env python3


class RecentCounter:
    def __init__(self):
        self.T = 3000
        self.pings = []
        self.last = 0

    def search(self, begin, end, t):
        while end - begin > 1:
            mid = (begin + end) // 2
            if t - self.pings[mid] <= self.T:
                end = mid
            else:
                begin = mid
        return begin if t - self.pings[begin] <= self.T else end

    def ping(self, t: int) -> int:
        self.pings.append(t)
        self.last = self.search(self.last, len(self.pings) - 1, t)
        return len(self.pings) - self.last


# Your RecentCounter object will be instantiated and called as such:
# obj = RecentCounter()
# param_1 = obj.ping(t)
