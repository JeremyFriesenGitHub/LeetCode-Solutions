class Solution:
    def canBeTypedWords(self, text: str, brokenLetters: str) -> int:
        
        words = text.split()
        count=0
        if len(brokenLetters) == 0:
            return len(words)
        for word in words:
            for i in range(len(brokenLetters)):
                if brokenLetters[i] in word:
                    break
                if brokenLetters[i] not in word and i == len(brokenLetters)-1:
                    count+=1
        return count
