class Solution:
    def maxArea(self, heights: List[int]) -> int:
        biggest = 0
        L = 0
        R = len(heights) - 1

        while L < R:
            cur = min(heights[L], heights[R]) * (R - L)
            biggest = max(biggest, cur)
            if heights[L] < heights[R]:
                L += 1
            else:
                R -= 1
        return biggest
