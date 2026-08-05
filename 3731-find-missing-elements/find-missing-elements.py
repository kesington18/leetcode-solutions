class Solution:
    def findMissingElements(self, nums: List[int]) -> List[int]:
        Arr = []
        maxN = max(nums)
        minN = min(nums)
        res = minN + 1
        while res <= maxN:
            if res not in nums:
                Arr.append(res)
            res += 1

        return Arr