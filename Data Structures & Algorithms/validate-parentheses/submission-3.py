class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        map = {"(": ")", "{": "}", "[": "]"}
        for ch in s:
            if ch in list(map.keys()):
                stack.append(ch)
            elif len(stack) <= 0 or map[stack.pop()] != ch:
                return False
        return len(stack) == 0
