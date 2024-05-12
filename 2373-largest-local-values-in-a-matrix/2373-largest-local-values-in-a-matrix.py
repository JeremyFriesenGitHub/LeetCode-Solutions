class Solution:
    def largestLocal(self, grid: List[List[int]]) -> List[List[int]]:
        n = len(grid)
        maxLocal = [[0] * (n-2) for _ in range(n-2)]
        for i in range(1,n-1):
            for j in range(1,n-1):
                for k in range(i-1,i+2):
                    for l in range(j-1,j+2):
                        spot = grid[k][l]
                        if spot > maxLocal[i-1][j-1]:
                            maxLocal[i-1][j-1]= spot
                        
        return maxLocal
        
        


        