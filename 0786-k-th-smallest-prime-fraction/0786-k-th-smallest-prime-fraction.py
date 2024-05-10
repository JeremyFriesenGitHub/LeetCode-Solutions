class Solution:
    def kthSmallestPrimeFraction(self, arr: List[int], k: int) -> List[int]:
        fractions=[]

        for i in range(len(arr)):
            for j in range(len(arr)):
                if i<j:
                    fractions.append(arr[i]/arr[j])

        sorted_fractions = sorted(fractions)
        for i in range(len(arr)):
            for j in range(len(arr)):
                if i<j:
                    if sorted_fractions[k-1] == (arr[i]/arr[j]):
                        return [arr[i], arr[j]]

        return [-1,-1]
        


        
