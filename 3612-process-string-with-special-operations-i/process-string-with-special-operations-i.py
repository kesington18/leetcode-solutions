class Solution:
    def processStr(self, s: str) -> str:
        res = []

        for char in s:
            if char == "#":
                res.extend(res)
            elif char == "*":
                if res:
                    res.pop()
            elif char == "%":
                res.reverse()
            else:
                res.append(char)

        return "".join(res)