class Solution:
    def sumZero(self, n: int) -> List[int]:
        if (n==1):
            return [0]

        else:
            arr = [-1]*n

            half = math.floor(n/2)
            otherHalf=0-half
            if(n%2!=0):
                arr[half]=0
            count=1
            for i in range(n):
                if (arr[i]!=0):
                    if (i<half):
                        arr[i]=otherHalf
                        otherHalf=otherHalf+1
                    else:
                        arr[i]=count
                        count=count+1
           
                
            return arr
            