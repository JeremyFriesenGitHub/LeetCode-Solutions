class Solution:
    def findMaxK(self, nums: List[int]) -> int:
        sorted_nums = sorted(nums, reverse=True)
        for num in sorted_nums:
            if -num in sorted_nums:
                return num
        return -1
        