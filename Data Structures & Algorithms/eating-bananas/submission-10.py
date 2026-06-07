class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        maximum = max(piles)
        L = 1
        R = maximum

        while L <= R:
            mid = (L + R) // 2
            hours = sum(math.ceil(pile / mid) for pile in piles)
            if hours > h:
                L = mid + 1
            else:
                R = mid - 1
        return L
