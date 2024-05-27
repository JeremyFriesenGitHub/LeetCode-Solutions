class Solution:
    def specialArray(self, nums: List[int]) -> int:
        
        for x in range(0, len(nums)+1):
            count=0
            for element in nums:
                if element >= x:
                    count+=1
            if count == x:
                return x
        return -1

        