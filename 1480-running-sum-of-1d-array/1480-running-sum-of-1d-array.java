class Solution {
    public int[] runningSum(int[] nums) {
        //running sum
        for (int i=0;i<nums.length;i++){
            if (i-1>=0){
                nums[i]=nums[i-1]+nums[i];
            }
        }
        return nums;
    }
}