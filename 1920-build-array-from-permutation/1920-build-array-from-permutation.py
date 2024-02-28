class Solution:
    def buildArray(self, nums: List[int]) -> List[int]:
        values=[0] * len(nums)
        for i in range(len(nums)):
            values[i] = nums[nums[i]]
        return values