class Solution:
    def rearrangeArray(self, nums: List[int]) -> List[int]:
        
        negative=[]
        positive=[]
        answer=[]
        for num in nums:
            if num <0:
                negative.append(num)
            else:
                positive.append(num)
        for i in range(len(negative)):
            answer.append(positive[i])
            answer.append(negative[i])
        return answer