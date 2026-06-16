class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s1) > len(s2):
            return False

        s1_freq = [0] * 26
        for ch in s1:
            s1_freq[ord(ch) - ord("a")] += 1

        s2_freq = [0] * 26
        for i in range(0, len(s1) - 1):
            s2_freq[ord(s2[i]) - ord("a")] += 1

        L = 0
        R = len(s1) - 1
        while R < len(s2):
            s2_freq[ord(s2[R]) - ord("a")] += 1
            if s1_freq == s2_freq:
                return True
            s2_freq[ord(s2[L]) - ord("a")] -= 1
            R += 1
            L += 1
        return False
