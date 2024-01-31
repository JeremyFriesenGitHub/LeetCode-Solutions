class Solution {
    public int[] dailyTemperatures(int[] temperatures) {
       Stack<Integer> stack = new Stack<Integer>();
       int[] result = new int[temperatures.length];
       stack.push(0);
       for (int i=1;i<temperatures.length;i++){
           while (!stack.empty() && temperatures[stack.peek()]<temperatures[i]){
               result[stack.peek()] = i -stack.peek();
               stack.pop();
           }
           stack.push(i);
       }
       while(!stack.empty()){
           result[stack.peek()]=0;
           stack.pop();
       }
       return result;

    }
}