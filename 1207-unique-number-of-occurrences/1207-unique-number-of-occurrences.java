class Solution {
    public boolean uniqueOccurrences(int[] arr) {
       Map<Integer,Integer> map = new HashMap<Integer,Integer>();
       for(int i=0;i<arr.length;i++){
           if (map.containsKey(arr[i])){
               int currentValue= map.get(arr[i]);
               map.put(arr[i],currentValue+1);
           }
           else{
               map.put(arr[i],1);
           }
        
       }
    //    System.out.println(map);
       HashSet<Integer> previousValues = new HashSet<>();
       for (int key : map.keySet()) {
           int value = map.get(key);
           if (previousValues.contains(value)) {
               return false;
            } else {
                previousValues.add(value);
            }
        }
        return true;

    // Set<Integer> previousValues = new HashSet<Integer>(map.values());
    // return previousValues.size()==map.size();
    }
}