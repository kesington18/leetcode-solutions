import math
class Solution:
    def maximumProduct(self, nums: List[int]) -> int:
        ''' res = []
        for i in nums:
            j = i + 1
            for j in nums:
                k = j + 1
                for  k in nums:
                    res.append(i * j * k)

        maxs = max(res)
        return maxs'''
        # print(nums)
        nums.sort()

        # print(nums)
        ind1 = 0
        ind2 = 1
        ind3 = 2
        indLast = -1
        res = 0
        arr = []

        # print(ind1)
        while ind3 < len(nums):
            if nums[ind1] < 0 and nums[ind2] < 0 and nums[indLast] > 0:
                res  = nums[ind1] * nums[ind2] * nums[indLast]
                arr.append(res)

            if nums[ind1] < 0 and nums[ind2] < 0 and nums[ind3] < 0:
                res  = math.prod(nums[-3:])
                arr.append(res)

            if nums[indLast] < 0:
                res  = math.prod(nums[-3:])
                arr.append(res)

            res = math.prod(nums[-3:])
            arr.append(res)
            ind3+=1

        maxs = max(arr)
        return maxs