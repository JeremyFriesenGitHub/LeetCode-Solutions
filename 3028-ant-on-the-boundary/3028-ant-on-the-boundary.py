class Solution:
    def returnToBoundaryCount(self, nums: List[int]) -> int:
        boundary=0
        count=0
        for i in range(len(nums)):
            step = nums[i]
            if step+boundary==0:
                count+=1
            boundary +=step
        return count
                
        