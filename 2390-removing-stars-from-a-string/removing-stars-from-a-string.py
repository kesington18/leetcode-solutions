class Solution:
    def removeStars(self, s: str) -> str:
        arr = []
       
        for char in s:
            #print(char)
            if char == "*":
                arr.pop()
            else:
                arr.append(char)
                
        return "".join(arr)