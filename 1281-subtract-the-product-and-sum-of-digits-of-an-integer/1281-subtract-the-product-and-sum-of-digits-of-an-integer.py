class Solution:
    def subtractProductAndSum(self, n: int) -> int:
        
        num=str(n)
        sum=0
        product=1
        for i in range(len(num)):
            digit = int(num[i])
            sum+=digit
            product*=digit
        return product-sum
            