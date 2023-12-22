class Solution:
    def maxScore(self, s: str) -> int:
       
        #init
        length= len(s)-1
        left=[0]*length
        right =[0]*length
        maxNums=[0]*length

        for i in range(length):
            if(i>0):
                left[i]= left[i-1] + s[i]
                right[i]= s[i+1:]

            else:
                left[i]=s[i]
                right[i]=s[i + 1:]
                
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
            maxNums[j]=countZeros+countOnes
        
        max=-1
        for m in range(len(maxNums)):
            if (max<maxNums[m]):
                max=maxNums[m]
        print(max)

        return max