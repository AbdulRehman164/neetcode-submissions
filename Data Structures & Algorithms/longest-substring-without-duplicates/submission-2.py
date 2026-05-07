class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        substr = set()
        res = 0
        L = 0
        for R in range(len(s)):
            while s[R] in substr:
                substr.remove(s[L])
                L += 1
            substr.add(s[R])
            res = max(res, R - L + 1)
        return res
