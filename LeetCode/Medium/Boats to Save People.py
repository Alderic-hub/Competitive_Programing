class Solution(object):
    def numRescueBoats(self, people, limit):
        ans = 0
        people = sorted(people)
        start = 0
        end = len(people)-1

        while start <= end:
            value = people[start] + people[end]
            if value <= limit:
                start += 1
            ans += 1
            end -= 1
        return ans
