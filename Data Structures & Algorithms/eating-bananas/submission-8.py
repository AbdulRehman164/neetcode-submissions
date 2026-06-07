import math
from typing import List


class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        maximum = max(piles)
        L = 1
        R = maximum

        while L <= R:
            mid = (L + R) // 2
            hours = h
            for pile in piles:
                hours -= math.ceil(pile / mid)
            if hours < 0:
                L = mid + 1
            else:
                R = mid - 1
        return L
