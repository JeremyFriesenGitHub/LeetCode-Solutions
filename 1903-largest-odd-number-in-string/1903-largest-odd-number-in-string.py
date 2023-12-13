class Solution:
    def largestOddNumber(self, num: str) -> str:

        #init stop value
        stop=-1

        #decreasing for loop on the string
        for i in range(len(num)- 1, -1,-1):
            digit=num[i]

            #convert digit to int
            digit=int(digit)
            
            #check if digit is odd and break
            if (digit % 2 !=0):
                stop=i
                break

        #if never odd, return ""
        if (stop==-1):
            return ""
        
        #if first index, return first index
        if (stop==0):
            return num[stop]
        
        #get all values in num until stop and return
        #init list to get result
        newStr=[]
        for j in range(0,stop+1):
            newStr.append(num[j])
        
    
        result = ''.join(newStr)
        return result
        

            

        