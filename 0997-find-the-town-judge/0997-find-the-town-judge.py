class Solution:
    def findJudge(self, n: int, trust: List[List[int]]) -> int:
        in_degree=[0] * n
        out_degree=[0] * n

        for i in range(len(trust)):
            
            out_value = trust[i][0]
            out_degree[out_value-1] +=1

            in_value = trust[i][1]
            in_degree[in_value-1]+=1
        
        for j in range(n):
    
            if in_degree[j] == n-1 and out_degree[j] == 0:
                return j+1
       
        return -1

            

        