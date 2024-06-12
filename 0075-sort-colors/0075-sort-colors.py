class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        #counts
        count0 = 0
        count1 = 0
        count2 = 0

        #loop1
        for i in range(len(nums)):
            if nums[i] == 0:
                count0+=1
            if nums[i] == 1:
                count1+=1
            if nums[i] == 2:
                count2+=1

        #loop2
        for j in range(len(nums)):
            if count0 > 0:
                nums[j] = 0
                count0-=1
            elif count1 > 0:
                nums[j] = 1
                count1-=1
            else:
                nums[j] = 2
            
        



        