class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        mapping = {"(": ")", "{": "}", "[": "]"}
        for ch in s:
            if ch in mapping:
                stack.append(ch)
            elif len(stack) == 0 or mapping[stack.pop()] != ch:
                return False
        return len(stack) == 0
