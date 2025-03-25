class Solution:
    def countPartitions(self, nums: List[int]) -> int:
        total1 = sum(nums)
        total2 = 0
        count = 0
        for i in range(len(nums) -1 ):
            total2 += nums[i]
            total1 -= nums[i]
            if (total1 - total2) % 2 == 0:
                count += 1
        return count




        