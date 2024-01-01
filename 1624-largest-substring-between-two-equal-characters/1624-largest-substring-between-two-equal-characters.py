class Solution:
    def maxLengthBetweenEqualCharacters(self, s: str) -> int:
        #init
        max=-1
        for i in range(len(s)):
            for j in range (len(s)):
                if (i<j):
                    if (s[i]==s[j]):
                        difference=j-i-1
                        if(difference>max):
                            max=difference
        return max


