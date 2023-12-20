class Solution {
    public int buyChoco(int[] prices, int money) {
        int min1 = Integer.MAX_VALUE;
        int min2 = Integer.MAX_VALUE;
        int savedIndex=-1;

        for (int i=0;i<prices.length;i++){
            if (prices[i]<min1){
                min1=prices[i];
                savedIndex=i;
                i=0;  
            }
            if(min2>prices[i] && prices[i]>=min1 && savedIndex!=i){
                min2=prices[i];
            }   
        }

        int newSum = money - min1 -min2;
        if (newSum >=0){
            // System.gc();
            return newSum;
        }
        // System.gc();
        return money;
    }
}