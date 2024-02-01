class Solution:
    def divideArray(self, nums: List[int], k: int) -> List[List[int]]:
        #need to sort
        nums.sort()
        listr=[]
        for i in range(len(nums)):
            if i-2>=0 and i%3==2:
                newList=[]
                if(nums[i]-nums[i-2]>k):
                    return []
                newList.append(nums[i-2])
                newList.append(nums[i-1])
                newList.append(nums[i])
                listr.append(newList)
        return listr