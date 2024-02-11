class Solution:
    def mostWordsFound(self, sentences: List[str]) -> int:
        #hmm
        count=1
        for sentence in sentences:
            sentenceCount=1
            for char in sentence:
                if char == " ":
                    sentenceCount+=1
            if sentenceCount>count:
                count=sentenceCount
            
        return count
        