class Solution:
    def heightChecker(self, heights: List[int]) -> int:
        count=0
        sorted_heights = sorted(heights)
        for i in range(len(sorted_heights)):
            if sorted_heights[i] != heights[i]:
                count+=1
        return count
        