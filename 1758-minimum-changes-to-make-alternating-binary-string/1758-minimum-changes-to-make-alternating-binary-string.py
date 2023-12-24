class Solution:
    def minOperations(self, s: str) -> int:
        #inits, for count 2, have to start at 1
        count1=0
        count2=1
        #init lists
        r1 = list(s)
        r2=list(s)
        #init starting bit
        start =s[0]

        #approach1 use start
        for i in range(len(s)):
            if (i>0):
                prev = r1[i-1]
                if (prev == r1[i]):
                    if(prev=="0"):
                        r1[i]="1"
                        count1=count1+1
                    if(prev=="1"):
                        r1[i]="0"
                        count1=count1+1
        
        #approach2 use the opposite of start
        if(start=="0"):
            r2[0]="1"
        if(start=="1"):
            r2[0]="0"
        for j in range(len(s)):
            if(j>0):
                prev = r2[j-1]
                if (prev == r2[j]):
                    if(prev=="0"):
                        r2[j]="1"
                        count2=count2+1
                    if(prev=="1"):
                        r2[j]="0"
                        count2=count2+1

        #return max count
        if(count1>count2):
            return count2
        return count1