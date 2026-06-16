class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        s1_sorted = "".join(sorted(s1))
        if len(s1) > len(s2):
            return False
        L = 0
        for R in range(len(s1), len(s2) + 1):
            if s1_sorted == "".join(sorted(s2[L:R])):
                return True
            L += 1
        return False
