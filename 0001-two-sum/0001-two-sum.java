import java.util.HashMap;

class Solution {
    public int[] twoSum(int[] nums, int target) {
        HashMap<Integer, Integer> map = new HashMap<>();
        
        for (int i = 0; i < nums.length; i++) {
            int complement = target - nums[i];
            
            // Check if the complement (the number needed to reach the target) is in the HashMap.
            if (map.containsKey(complement)) {
                return new int[]{map.get(complement), i};
            }
            
            // Add the current number and its index to the HashMap.
            map.put(nums[i], i);
        }
        
        // If no solution is found, return an empty array or handle the case as needed.
        return new int[0];
    }
}
