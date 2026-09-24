class Solution:
    def minLengthAfterRemovals(self, nums: List[int]) -> int:
        n = len(nums)
        l, r = 0, (n+1) // 2
        count = 0

        while l < (n+1) // 2 and r < n:
            if nums[l] < nums[r]:
                count += 2
                l += 1
            r += 1
        return n - count