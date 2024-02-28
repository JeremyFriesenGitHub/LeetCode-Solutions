class Solution:
    def minimumSum(self, num: int) -> int:
        newnum = str(num)
        sorted_digits = sorted(str(num))
        pair1 = int(sorted_digits[0] + sorted_digits[2])
        pair2 = int(sorted_digits[1] + sorted_digits[3])
        return pair1+pair2
    
                    
                    
                