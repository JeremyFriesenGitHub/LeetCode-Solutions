class Solution:
    def climbStairs(self, n: int) -> int:
        # recursion
        # for all n>2; f(n)=f(n-1)+f(n-2)
        # f(1)=1, f(2)=2
        # can do an induction hypothesis 
        #this is ok, but we want to solve this with iteration
        #lets graph this table:
        #x=1,2,3,4,5,6,7,8,9
        #y=1,2,3,5,8,13,21,34,51
        #ahha, this is the fibonacci sequence, no?, to verify, yes it is
        #we can plug its mathematical equation instead!

        #f(n)= (golden_ratio^n -ugly_little_brother^n)/sqrt(5)

        #golden_ratio = 1+sqrt(5)/2
        #ugly_little_brother = 1-sqrt(5)/2

        #lets implement this!:

        golden_ratio = (1+sqrt(5))/2
        ugly_little_brother = (1-sqrt(5))/2
        answer = ((golden_ratio ** (n+1)) -(ugly_little_brother**(n+1)))/sqrt(5)
        #answer needs to floor, for floating points and somehow need n+1, idk why
        return int(answer)