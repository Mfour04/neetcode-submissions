class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack= []
        for c in tokens:
            if c not  in "+-*/":
                stack.append(int(c))
            else:
                b = stack.pop()
                a = stack.pop()

                if c == "+":
                    stack.append(a + b)
                elif c == "-":
                    stack.append(a - b)
                elif c == "*":
                    stack.append(a * b)
                elif c == "/":
                    stack.append(int(a/b))
        return  stack[0]