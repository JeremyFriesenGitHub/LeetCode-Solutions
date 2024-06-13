class Solution:
    def minMovesToSeat(self, seats: List[int], students: List[int]) -> int:
        
        sorted_seats = sorted(seats)
        sorted_students = sorted(students)
        count=0
        for i in range(len(sorted_students)):
            count+=abs(sorted_seats[i] - sorted_students[i])
        return count
