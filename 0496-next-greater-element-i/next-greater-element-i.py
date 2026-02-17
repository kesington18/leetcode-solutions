from typing import List

class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        res = []

        for num in nums1:
            newInd = nums2.index(num)
            nextGreater = -1

            for i in range(newInd + 1, len(nums2)):
                if nums2[i] > nums2[newInd]:
                    nextGreater = nums2[i]
                    break

            res.append(nextGreater)

        return res
