class Solution {
    public int majorityElement(int[] nums) {
        
        int max=Integer.MIN_VALUE;
        Map<Integer,Integer> map = new HashMap<Integer,Integer>();
        for (int i=0;i<nums.length;i++){
            if (map.containsKey(nums[i])){
                int value = map.get(nums[i]);
                if (value+1>max){
                    max=value+1;
                }
                map.put(nums[i],value+1);
            }
            else{
                if(max == Integer.MIN_VALUE){
                    max=1; 
                }
                map.put(nums[i],1);
                
            }
        }
        for (Map.Entry<Integer, Integer> entry : map.entrySet()) {
        if (max == entry.getValue()) {
            return entry.getKey(); 
        }
        }
    return -1;
    }
}