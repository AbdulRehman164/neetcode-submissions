class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        count = {}
        L = 0
        maxFreq = 0
        best = 0
        for R in range(len(s)):
            count[s[R]] = count.get(s[R], 0) + 1
            maxFreq = max(maxFreq, count[s[R]])
            while (R - L + 1) - maxFreq > k:
                count[s[L]] -= 1
                L += 1
            best = max(best, R - L + 1)
        return best
