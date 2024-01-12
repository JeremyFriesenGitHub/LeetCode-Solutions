class Solution:
    def halvesAreAlike(self, s: str) -> bool:
        
        #length and half vars
        half=int(len(s)/2)
        length=len(s)
        
        #vowels array
        vowels=['a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U']
        
        #counting variables to keep track of vowels
        count1=0
        count2=0
        
        #loop half and count vowels
        for i in range(half):
            if s[i] in vowels:
                count1=count1+1

        #loop other half and count vowels
        for j in range(half,length):
            if s[j] in vowels:
                count2=count2+1
        
        #return true iff count1==count2, and false otherwise
        return count1==count2