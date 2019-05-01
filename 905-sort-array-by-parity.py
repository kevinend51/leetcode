from itertools import chain


class Solution:
    def sortArrayByParity(self, A: List[int]) -> List[int]:
        even = filter(lambda a: a % 2 == 0, A)
        odd = filter(lambda a: a % 2 == 1, A)
        return list(chain(even, odd))
