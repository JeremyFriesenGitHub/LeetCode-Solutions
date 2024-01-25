class Solution:
    def fib(self, n: int) -> int:
        
        # easy solution
        # if n>1:
        #     return self.fib(n-1)+self.fib(n-2)
        # else:
        #     return n


        #hard to find solution
        golden= (1+sqrt(5))/2 
        ugly = (1-sqrt(5))/2

        return int((golden**n - ugly**n) / sqrt(5))
