class Solution:
    def checkDivisibility(self, n: int) -> bool:
        n = str(n)
        ads = 0
        ams = 1

        for i in n:
            ads = ads + int(i)
        
        for i in n:
            ams = ams * int(i)
        
        total = ams + ads
        
        if int(n) % total == 0:
            return True
        else: 
            return False