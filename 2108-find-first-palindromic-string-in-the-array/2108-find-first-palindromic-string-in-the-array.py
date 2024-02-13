class Solution:
    def firstPalindrome(self, words: List[str]) -> str:
        for i in range(len(words)):
            if self.isPalindrome(words[i]):
                return words[i]
        return ""

        
    def isPalindrome(self, s: string)->bool:
        for i in range(len(s) // 2):
            if s[i] != s[~i]:
                return False
        return True
    

        