class Solution:
    def restoreString(self, s: str, indices: List[int]) -> str:
        newStr=[0]*len(indices)
        for i in range(len(indices)):
            newStr[indices[i]]= s[i]
        newStr=''.join(newStr)
        return newStr