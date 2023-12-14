class Solution:
    def onesMinusZeros(self, grid: List[List[int]]) -> List[List[int]]:
        
        #init diff
        rows=len(grid)
        cols=len(grid[0])
        diff = [[0 for _ in range(cols)] for _ in range(rows)]
        
        #init arrays
        onesRow=[0 for _ in range(rows)]
        zerosRow=[0 for _ in range(rows)]
        onesCol=[0 for _ in range(cols)]
        zerosCol=[0 for _ in range(cols)]

        #traverse rows
        for row in range(len(grid)):
            zerosCounter=0
            onesCounter=0
            for col in range(len(grid[0])):
                # traverses the row until col reaches len(grid[0])
                #print(grid[row][col])
                
                #if at the end of the row, count and then add to arrays
                if (col-(len(grid[0])-1)==0):
                    if(grid[row][col]==0):
                        zerosCounter=zerosCounter+1
                        zerosRow[row]=zerosCounter
                        onesRow[row]=onesCounter
                    else:
                        onesCounter=onesCounter+1
                        zerosRow[row]=zerosCounter
                        onesRow[row]=onesCounter
                
                #otherwise, just count
                else:
                    if(grid[row][col]==0):
                        zerosCounter=zerosCounter+1
                    else:
                        onesCounter=onesCounter+1
        
        

        #traverse cols
        for col in range(len(grid[0])):
            zerosCounter=0
            onesCounter=0
            for row in range(len(grid)):
                # col until row=row+1
                #print(grid[row][col])
                
                #if at the end of the row, count and then add to arrays
                if (row-(len(grid)-1)==0):
                    if (grid[row][col]==0):
                        zerosCounter=zerosCounter+1
                        zerosCol[col]=zerosCounter
                        onesCol[col]=onesCounter
                    else:
                        onesCounter=onesCounter+1
                        zerosCol[col]=zerosCounter
                        onesCol[col]=onesCounter
                
                #otherwise, just count
                else:
                    if (grid[row][col]==0):
                        zerosCounter=zerosCounter+1
                    else:
                        onesCounter=onesCounter+1
        

        #result for diff
        for i in range(len(diff)):
            for j in range(len(diff[0])):
                diff[i][j]=onesRow[i]+onesCol[j]-zerosRow[i]-zerosCol[j]
        

        #return diff array
        return diff