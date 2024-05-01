class Solution:
    def reversePrefix(self, word: str, ch: str) -> str:
        
        count=0
        for char in word:
            if char == ch:
                prefix = word[:count+1]
                reversed_prefix = prefix[::-1]
                word = word.replace(prefix, reversed_prefix, 1)
                return word
            else:
                count+=1
        return word