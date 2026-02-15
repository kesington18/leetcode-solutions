class Solution:
    def thirdMax(self, nums: List[int]) -> int:
        unique = list(set(nums))

        unique.sort(reverse = True)

        if len(unique) < 3:
            return unique[0]

        return unique[2]