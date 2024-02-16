class Solution:
    def largestPerimeter(self, nums: List[int]) -> int:
        nums.sort(reverse=True)
        for i in range(len(nums)-2):
            largest = nums[i]
            rest = sum(nums[j] for j in range(i+1,len(nums)))
            if largest<rest:
                return largest+rest
        return -1