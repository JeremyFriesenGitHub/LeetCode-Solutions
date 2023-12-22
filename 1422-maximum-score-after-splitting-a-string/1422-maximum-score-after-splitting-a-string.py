class Solution:
    def maxScore(self, s: str) -> int:
       
        #init
        length= len(s)-1
        left=[0]*length
        right =[0]*length
        maxNums=[0]*length
        
        #set left and right arrays
        for i in range(length):
            if(i>0):
                
                left[i]= left[i-1] + s[i]
                right[i]= s[i+1:]

            else:
                
                left[i]=s[i]
                right[i]=s[i + 1:]
                
        #count the ones and zeros in left and right array
        for j in range(len(left)):
            
            stringLeft=left[j]
            stringRight=right[j]
            countZeros=0
            countOnes=0
            
            for k in range(len(stringLeft)):
                
                if (stringLeft[k]=="0"):
                    countZeros=countZeros+1
                    
            for l in range(len(stringRight)):
                
                if (stringRight[l]=="1"):
                    countOnes=countOnes+1
            
            #add both counts to the max array
            maxNums[j]=countZeros+countOnes
        
        
        #max 
        max=-1
        
        #get max 
        for m in range(len(maxNums)):
            
            if (max<maxNums[m]):
                max=maxNums[m]
        #return
        return max