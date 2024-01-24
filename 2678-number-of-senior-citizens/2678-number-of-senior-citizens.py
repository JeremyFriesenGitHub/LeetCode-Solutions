class Solution:
    def countSeniors(self, details: List[str]) -> int:
        #countSeniors
        count =0
        for string in details:
            age =string[11] +string[12]
            if age>str(60):
                count+=1
        
        return count