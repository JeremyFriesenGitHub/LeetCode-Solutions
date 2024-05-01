class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        #binary search algorithm
        
        middleIndex = len(nums)//2

        leftIndex = 0
        rightIndex = len(nums)-1

        if target == nums[middleIndex]:
            return middleIndex
        
        flag = True

        while (leftIndex <= rightIndex):
            if target == nums[leftIndex]:
                return leftIndex

            if target == nums[rightIndex]:
                return rightIndex

            if target == nums[middleIndex]:
                return middleIndex

            if target < nums[middleIndex]:
                rightIndex = middleIndex - 1
                middleIndex = rightIndex // 2
                
            if target > nums[middleIndex]:
                leftIndex = middleIndex + 1
                middleIndex = (rightIndex + leftIndex)//2
            
        return leftIndex



            
            


            

            
            


