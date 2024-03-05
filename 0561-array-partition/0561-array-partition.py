class Solution:
    def arrayPairSum(self, nums: List[int]) -> int:
        sorted_nums=sorted(nums)
        total_sum = 0
        for i in range(0,len(sorted_nums) - 1,2):  
            mini = min(sorted_nums[i], sorted_nums[i+1])
            total_sum += mini
        return total_sum
