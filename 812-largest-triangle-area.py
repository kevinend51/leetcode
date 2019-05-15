#!/usr/bin/env python3

from itertools import combinations as cmb


class Solution:
    def calc_dist(self, p0, p1):
        return ((p0[0] - p1[0])**2 + (p0[1] - p1[1])**2)**0.5

    def calc_area(self, p0, p1, p2):
        a = self.calc_dist(p0, p1)
        b = self.calc_dist(p1, p2)
        c = self.calc_dist(p2, p0)
        a, b, c = sorted([a, b, c])
        if a + b < c:
            return 0
        s = (a + b + c) / 2
        return (s*(s - a)*(s - b)*(s - c))**0.5

    def largestTriangleArea(self, points: List[List[int]]) -> float:
        return max(self.calc_area(p0, p1, p2) for p0, p1, p2 in cmb(points, 3))
