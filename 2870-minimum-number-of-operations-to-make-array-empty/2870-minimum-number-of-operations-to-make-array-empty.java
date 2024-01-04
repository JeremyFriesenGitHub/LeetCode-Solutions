class Solution {
    public int minOperations(int[] nums) {
        Map<Integer,Integer> map = new HashMap<Integer,Integer>();

        for (int i=0;i<nums.length;i++){
            int num= nums[i];
            if (map.containsKey(num)){
                int currentValue = map.get(num);
                map.put(num,currentValue+1);
            }
            else{
                map.put(num,1);
            }
        }
        //System.out.println(map);
        int numOperations=0;
         for (Map.Entry<Integer, Integer> entry : map.entrySet()){
                int key = entry.getKey();
                //System.out.println(key);
                int value = entry.getValue();
                if(value%3==0){
                    numOperations=numOperations+(value/3);
                }
                //second check
                else if(value%3==1 && value>3){
                    int result = (int) Math.floor((double) value / 3);
                    result=result-1;
                    numOperations=numOperations+2+result;
                }
                else if(value%3==2 && value>3){
                    int result = (int) Math.floor((double) value / 3);
                    numOperations=numOperations+1+result;

                }
                else if (value==2){
                    numOperations=numOperations+1;
                }
                else{
                    return -1;
                }
         }
        return numOperations;
        

    }
}