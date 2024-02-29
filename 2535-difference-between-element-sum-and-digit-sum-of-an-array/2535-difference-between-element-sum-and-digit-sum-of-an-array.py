class Solution:
    def differenceOfSum(self, nums: List[int]) -> int:
        elmnt=0
        dig=0
        for i in range(len(nums)):
            elmnt+=nums[i]
            
            digits = str(nums[i])
            for digit in digits:
                dig+=int(digit)
            
        return abs(elmnt - dig)
            