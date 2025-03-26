class Solution:
    def maximumNumberOfStringPairs(self, words: List[str]) -> int:
        count = 0 
        for i in range(len(words)):

            map1 = Counter(words[i])

            for j in range(len(words)):
                if i < j:
                    map2 = Counter(words[j])

                    if map1 == map2:
                        count+=1
        return count
        