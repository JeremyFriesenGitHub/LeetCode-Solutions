class Solution:
    
    def countSubstrings(self, s: str) -> int:
        listr=[]
        listr= self.get_all_substrings(s)
        count=0
        for i in range(len(listr)):
            if self.isPalindrome(listr[i]):
                count+=1
        return count
    

    def get_all_substrings(self, s:str)->List[str]:
        substrings = []
        length = len(s)
        for start in range(length):
            for end in range(start + 1, length + 1):
                substring = s[start:end]
                substrings.append(substring)
        return substrings

    
    def isPalindrome(self, s: str) -> bool:
        for i in range(len(s) // 2):
            if s[i] != s[-(i+1)]: 
                return False
        return True

    def isEven(self, s:str)-> bool:
        length=len(s)
        if (length%2==0):
            return True
        else:
            return False