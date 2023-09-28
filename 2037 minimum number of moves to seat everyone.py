class Solution:
    def minMovesToSeat(self, seats: List[int], students: List[int]) -> int:
        '''
        algo:
        1. sort both the lists
        2. find the element wise difference and then sum it and then return this sum
        '''
        seats = sorted(seats)
        students = sorted(students)

        result = 0

        for i in range(len(seats)):
            result += abs(seats[i] - students[i])
        
        return result