class Solution(object):
    def minMovesToSeat(self, seats, students):
        seats.sort()
        students.sort()
        ans = 0
        for n in range(len(seats)):
            val = abs(seats[n]-students[n])
            ans += val
        return ans
        
