class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        count = 1
        j = 1

        for j in range(1, len(nums)):
            if nums[j] != nums[j - 1]:
                nums[count] = nums[j]
                count += 1

        return count