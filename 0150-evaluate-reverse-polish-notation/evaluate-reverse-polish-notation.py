class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        res = []

        for token in tokens:

            if token in ('+', '-', '*', '/'):
                b = res.pop()
                a = res.pop()

                if token == "+":
                    res.append(a + b)
                elif token == "-":
                    res.append(a - b)
                elif token == "*":
                    res.append(a * b)
                elif token == "/":
                    res.append(int(a / b))
            else:
                res.append(int(token))
        
        return res[0]