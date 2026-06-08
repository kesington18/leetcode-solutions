class Solution:
    def calPoints(self, operations: List[str]) -> int:
        sign = ["+","D", "C"]
        res = []

        for i in operations:
            if i not in sign:
                res.append(int(i))
            elif i == "+":
                res.append(sum(res[-2:]))
            elif i == "D":
                res.append(res[-1] * 2)
            elif i == "C":
                res.pop()
            
        return sum(res)