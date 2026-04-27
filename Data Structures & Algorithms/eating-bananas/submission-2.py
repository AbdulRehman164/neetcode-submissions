import math


class Solution:
    def isValid(self, num, hours, piles):
        for pile in piles:
            hours -= math.ceil(pile / num)
            if hours < 0:
                return False
        return True

    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        L = 1
        R = max(piles)
        while L <= R:
            mid = (L + R) // 2
            if self.isValid(mid, h, piles):
                R = mid - 1
            else:
                L = mid + 1
        return L
