class Solution:
    def frequencySort(self, s: str) -> str:
        #set
        set1=[]
        set2=[]

        for i in range(len(s)):
            if s[i] not in set2:
                set2.append(s[i])
                set1.append(1)
            else:
                for j in range(len(set2)):
                    if set2[j] ==s[i]:
                        value=set1[j]
                        value=value+1
                        set1[j]=value

        combined = list(zip(set1, set2))
        combined_sorted = sorted(combined,reverse=True)
        list1_sorted, list2_sorted = zip(*combined_sorted)

        
        set1 = list(list1_sorted)
        set2 = list(list2_sorted)

        string=""

        for k in range(len(set1)):
            for _ in range(0,set1[k]):
                string=string+set2[k]
        
        return string


        