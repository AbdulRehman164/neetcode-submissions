class Solution:
    def maxArea(self, heights: List[int]) -> int:
        res = 0
        L = 0
        R = len(heights) - 1
        while L < R:
            cur = (R - L) * min(heights[L], heights[R])
            if heights[L] < heights[R]:
                L += 1
            else:
                R -= 1
            res = max(res, cur)
        return res
