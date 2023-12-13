class Solution:
    def totalMoney(self, n: int) -> int:

        #array to simulate a weekly deposit
        week=[1,2,3,4,5,6,7]
        
        #using long division to get number of weeks where you deposited money throughout the entire week
        numOfCompleteWeeks= (n//7)

        #number of days left in the last week
        numberOfLastDays = n%7

        #set total 
        total =0
      
        #calculate sum of all the daily deposits for 'complete' weeks
        for numWeeks in range(numOfCompleteWeeks):
            for day in range(len(week)):
                total=numWeeks+week[day]+total
                

        #base case where you don't deposit money for a 'complete' week
        if (numOfCompleteWeeks==0 ):
            for day in range(numberOfLastDays):
                total=total+week[day]

        #case for the last few days left to calculate 
        if (numOfCompleteWeeks>0):
            for day in range(numberOfLastDays):
                total=total+week[day]+numOfCompleteWeeks
        
        return total

