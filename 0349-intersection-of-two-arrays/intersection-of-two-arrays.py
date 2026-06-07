class Solution:
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        neset = set(nums1)
        res = []

        for n in nums2:
            if n in neset: 
                res.append(n)
                neset.discard(n)
    
        return res