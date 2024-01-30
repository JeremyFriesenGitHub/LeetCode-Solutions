class Solution {
    public int evalRPN(String[] tokens) {
        //the essential stack
        Stack<Integer> stack = new Stack<Integer>();
        
        //operators
        String[] operators = new String[4];
        operators[0]= "+";
        operators[1]= "-";
        operators[2]= "*";
        operators[3]= "/";

        //essentially essential
        for (int i=0;i<tokens.length;i++){
            if (!tokens[i].equals(operators[0]) && !tokens[i].equals(operators[1]) && !tokens[i].equals(operators[2]) && !tokens[i].equals(operators[3])){
                int value = Integer.parseInt(tokens[i]);
                stack.push(value);
            }

            //using the notation, pop stack
            else{
                int value1 = stack.pop();
                int value2 = stack.pop();
                if (tokens[i].equals(operators[0])){
                    int result = value2+value1;
                    stack.push(result);
                }
                if (tokens[i].equals(operators[1])){
                    int result = value2-value1;
                    stack.push(result);
                }
                if (tokens[i].equals(operators[2])){
                    int result = value2*value1;
                    stack.push(result);
                }
                if (tokens[i].equals(operators[3])){
                    int result = value2/value1;
                    stack.push(result);
                }
            }
        }
        //return most recent result
        return stack.peek();   
    }
}