class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        for token in tokens:
            try:
                stack.append(int(token))
            except:
                b = stack.pop()
                a = stack.pop()
                if token == "+":
                    stack.append(a + b)
                elif token == "*":
                    stack.append(a * b)
                elif token == "-":
                    stack.append(a - b)
                elif token == "/":
                    stack.append(int(a / b) if b != 0 else 0)
        return stack[-1]
