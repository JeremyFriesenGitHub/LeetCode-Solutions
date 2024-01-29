class MyQueue {
    private Stack<Integer> stack1;
    private Stack<Integer> stack2;
    public MyQueue() {
    this.stack1 = new Stack<Integer>();
    this.stack2 = new Stack<Integer>();
    }
    
    public void push(int x) {
         while (!stack1.isEmpty()) {
            stack2.push(stack1.pop());
        }

        stack1.push(x);

        while (!stack2.isEmpty()) {
            stack1.push(stack2.pop());
        }
    }
    
    
    public int pop() {
        int value = stack1.pop();
        return value;
    }
    
    public int peek() {
        int value = stack1.peek();
        return value;  
    }
    
    public boolean empty() {
        if (stack1.isEmpty() && stack2.isEmpty()){
            return true;
        }
        return false;
    }
}

/**
 * Your MyQueue object will be instantiated and called as such:
 * MyQueue obj = new MyQueue();
 * obj.push(x);
 * int param_2 = obj.pop();
 * int param_3 = obj.peek();
 * boolean param_4 = obj.empty();
 */