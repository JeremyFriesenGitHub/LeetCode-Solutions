class Solution:
    def getCommon(self, nums1: List[int], nums2: List[int]) -> int:
        set1=set(nums1)
        set2=set(nums2)
        
        return min(set1.intersection(set2)) if set1.intersection(set2) else -1