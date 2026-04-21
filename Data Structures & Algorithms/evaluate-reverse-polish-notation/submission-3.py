class Solution:
    def evaluate(self, a, b, operator):
        if operator == "+":
            return a + b

        if operator == "-":
            return a - b

        if operator == "*":
            return a * b

        if operator == "/":
            return int(a / b)

    def evalRPN(self, tokens: List[str]) -> int:
        operators = {"+", "-", "*", "/"}
        stack = []
        for token in tokens:
            if token in operators:
                b = stack.pop()
                a = stack.pop()
                result = self.evaluate(a, b, token)
                stack.append(result)
            else:
                stack.append(int(token))
        return stack.pop()
