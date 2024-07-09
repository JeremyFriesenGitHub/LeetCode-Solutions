class Solution:
    def averageWaitingTime(self, customers: List[List[int]]) -> float:
        
        currentTime = 0
        waitTime = 0

        for arrivalTime, timeToPrepare in customers:
            if currentTime < arrivalTime:
                currentTime = arrivalTime

            currentTime += timeToPrepare 
            waitTime += currentTime - arrivalTime
        
        return waitTime/len(customers)

