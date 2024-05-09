class Solution:
    def findRelativeRanks(self, score: List[int]) -> List[str]:
        reverse_score = sorted(score, reverse = True)
        output_medals = []

        for i in range(len(score)):
            for j in range(len(reverse_score)):
                if reverse_score[j] == score[i]:
                    if j == 0:
                        output_medals.append("Gold Medal")
                    elif j == 1:
                        output_medals.append("Silver Medal")
                    elif j == 2:
                        output_medals.append("Bronze Medal")
                    else:
                        output_medals.append(str(j+1))
        return output_medals

        
        
        