class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        brackets = {"(": ")", "{": "}", "[": "]"}
        for ch in s:
            if ch in brackets:
                stack.append(ch)
            elif len(stack) <= 0 or brackets[stack.pop()] != ch:
                return False
        return len(stack) == 0
