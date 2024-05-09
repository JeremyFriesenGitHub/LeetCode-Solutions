class Solution:
    def maximumHappinessSum(self, happiness: List[int], k: int) -> int:
        sorted_happiness = sorted(happiness, reverse = True)
        greedy_answer = 0

        for i in range(k):
            if sorted_happiness[i] - i >= 0:
                greedy_answer += sorted_happiness[i] - i
        
        return greedy_answer


       
            
            