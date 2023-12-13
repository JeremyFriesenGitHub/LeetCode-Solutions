class Solution:
    def hammingWeight(self, n: int) -> int:
        
      
        binary = '{0:08b}'.format(n)
        count =0
        for i in range(len(binary)):
            if (binary[i] == '1'):
                count=count+1
        return count