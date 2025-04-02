class Solution:
    def maximumTripletValue(self, nums: List[int]) -> int:
        max = 0 
        for i in range(len(nums)):
            for j in range(len(nums)):
                for k in range(len(nums)):
                    if k > j and j > i :
                        if max < (nums[i] - nums[j]) * nums[k]:
                            max = (nums[i] - nums[j]) * nums[k]
        return max

        