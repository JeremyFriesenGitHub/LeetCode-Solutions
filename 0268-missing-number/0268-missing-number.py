class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        
        actual_sum = sum(nums)
        hypothetical_sum = ((len(nums))* (len(nums)+1))//2
        return hypothetical_sum - actual_sum 