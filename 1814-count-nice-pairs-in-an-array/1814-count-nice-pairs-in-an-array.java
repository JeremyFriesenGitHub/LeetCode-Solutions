class Solution {
    public int countNicePairs(int[] nums) {
        //array of nums
        //reverse(x)= reverse of the non negative integer x
        //123 ==321, 120==21
        //pair is nice if:
        // i<j and nums[i]+ reverse(nums[j])== nums[j] + reverse(nums[i])

        //so implement reverse
        //create a nested for loop for size of the array
        // check if nice (if i<j and if )
        //increment a counter
        //return the counter with % 1000000007;

        //might run into TLE; 
        //return answer % 1000000007;

        //create vars
        Map<Integer, Integer> map = new HashMap<>();
        long count = 0;
        final int MOD = 1000000007;

        // Calculate the difference and store in the map
        //for each integer (num) in nums
        for (int num : nums) {
            //difference=the number - the reverse number
            int diff = num - reverse(num);
            //store the difference as a key with it frequency value
            map.put(diff, map.getOrDefault(diff, 0) + 1);
        }
        
        // Count the pairs
        //for each value in  map
        for (int value: map.values()) {
           
           //dont understand this line: 
            //formula for count? 
            count += ((long)value * (value - 1) / 2); 
        }

        // return with mod
        count = count %MOD;
        System.gc();
        return (int) count;
    }

       
    //logic for reverse
    public int reverse(int num){
        int reverse=0;
        while(num != 0) {
            int remainder = num % 10;  
            reverse = reverse * 10 + remainder;
            num = num/10;
            }
            return reverse;

    }
}