class Solution:
    def findWordsContaining(self, words: List[str], x: str) -> List[int]:
        
        array=[]
        
        for i in range(len(words)):
            
            if x in words[i]:
                
                array.append(i)
                
        return array
                