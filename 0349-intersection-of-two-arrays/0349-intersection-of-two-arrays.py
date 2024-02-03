class Solution:
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        #intersection, items must be unique, not just in
        result=[]
        length1= len(nums1)
        length2=len(nums2)

        if length2<length1:
            for i in range(length2):
                if nums2[i] in nums1 and nums2[i] not in result:
                    result.append(nums2[i])
           
        else:
            for i in range(length1):
                if nums1[i] in nums2 and nums1[i] not in result:
                    result.append(nums1[i])

        return result

     
                    