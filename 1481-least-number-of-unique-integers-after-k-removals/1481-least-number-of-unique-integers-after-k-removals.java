class Solution {
    public int findLeastNumOfUniqueInts(int[] arr, int k) {
        //answer
        Map<Integer,Integer> map = new HashMap<Integer,Integer>();
        for (int i=0;i<arr.length;i++){
            if (map.containsKey(arr[i])){
                int value = map.get(arr[i]);
                map.put(arr[i],value+1);
            }
            else{
                map.put(arr[i],1);
            }
        }
        List<Integer> list = new ArrayList<Integer>(map.values());
        Collections.sort(list);
        System.out.println(list);
        
        int index=0;
        for (int j=0;j<k;j++){
            int value=list.get(index);
            if (value==1){
                list.remove(index);
            }
            else{
                value=value-1;
                list.set(index, value);
            }
        }
        return list.size();

    }
}