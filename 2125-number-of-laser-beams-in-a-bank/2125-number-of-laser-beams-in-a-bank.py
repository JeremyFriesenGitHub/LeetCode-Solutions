class Solution:
    def numberOfBeams(self, bank: List[str]) -> int:
        
        array=[0]*len(bank)
        newArray=[]
        for i in range(len(bank)):
            count=0
            for j in range(len(bank[0])):
                if bank[i][j]=="1":
                    count=count+1
                    array[i]=count
        
        result =0
        for k in range(len(array)):
            if array[k]>0:
                newArray.append(array[k])
        #base case
        if(len(newArray)<=1):
            return 0

            
        for l in range(1, len(newArray)):
            result = (newArray[l] * newArray[l - 1]) + result
        return result
