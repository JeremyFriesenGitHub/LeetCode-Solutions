class Solution:
    def firstUniqChar(self, s: str) -> int:
        index =-1
        if(len(s)==1):
            return 0
        for i in range(len(s)):
            for j in range(len(s)):
                if i!=j:
                    if s[i] == s[j]:
                        break
                    if s[i]!=s[j] and j == len(s)-1 or (i==len(s)-1 and s[i]!=s[j] and j==len(s)-2 ):
                        index=i
                        return index                
        return index