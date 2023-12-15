class Solution:
    def destCity(self, paths: List[List[str]]) -> str:
        #if unique and index is [1], thats oour destination city
        #terribly inefficient

        #init uniqueStr
        uniqueStr=[" "]* len(paths)* 2
        count=0
        
        #flatten paths
        for row in range(len(paths)):
            for col in range(len(paths[row])):
                uniqueStr[count]=paths[row][col]
                count=count+1

        #find uniqueStrings
        for i in range(len(uniqueStr)):
            oldString=uniqueStr[i]
            uniqueStr[i]=""
            
            #if oldString unique
            if oldString  not in uniqueStr:
                #if index is odd
                if (i %2 !=0):
                    #answer
                    return oldString
            #if not unique, eliminate other instance in arr
            else:
                for j in range(len(uniqueStr)):
                    if (oldString == uniqueStr[j]):
                        uniqueStr[j]=""
                        
        #global return if nothing happens    
        return ""


        