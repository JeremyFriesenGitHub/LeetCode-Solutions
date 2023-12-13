class Solution {
    public int findSpecialInteger(int[] arr) {
        // System.out.println(arr.length);
        for (int i=0;i<arr.length;i++){
           int count=0;
            for (int j=0;j<arr.length;j++){
                int num= arr[i];
                if (arr[j]==num){
                    count++;
                }
                if (((float) count/(float) arr.length)>0.25){
                    System.gc();
                    return num;
                }
            }
        }
        System.gc();
        return -1;
    }
}