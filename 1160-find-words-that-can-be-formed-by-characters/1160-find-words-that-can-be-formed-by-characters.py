class Solution:
    def countCharacters(self, words: List[str], chars: str) -> int:
        def replace_character_at_index(word, index, new_character):
            if index < 0 or index >= len(word):
                return word
            new_word = word[:index] + new_character + word[index + 1:]
            return new_word

        
        count =0
        chars = list(chars)
        for word in words:
            newList= chars.copy()
            newCount=0
           # print(len(word))
            for i in range(len(newList)):
              
                    if newList[i] in word:
                        index= word.index(newList[i])
                        #print(type(word))
                        word = replace_character_at_index(word,index,"#")
                       # print(word)
                       # print(newList)
                        newList[i]=""
                        
                      #  print(newList)
                        newCount=newCount+1
                      #  print(newCount)
                    if (newCount==len(word)):
                        count +=len(word)
                        break

        return count