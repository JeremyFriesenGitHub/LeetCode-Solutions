class Solution:
    def maxProductDifference(self, nums: List[int]) -> int:
        sorted_nums=sorted(nums)
        min1= sorted_nums[0]
        min2= sorted_nums[1]
        max1=sorted_nums[len(sorted_nums)-1]
        max2=sorted_nums[len(sorted_nums)-2]
        product_difference = (max1 * max2) - (min1 * min2)
        return product_difference