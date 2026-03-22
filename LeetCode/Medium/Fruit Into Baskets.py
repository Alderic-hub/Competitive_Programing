class Solution(object):
    def totalFruit(self, fruits):
        max_fruits = 0
        start = 0
        last_seen = {}

        for end in range(len(fruits)):
            last_seen[fruits[end]] = end

            if len(last_seen) > 2:
                oldest = min(last_seen.values())
                del last_seen[fruits[oldest]]
                start = oldest + 1

            max_fruits = max(max_fruits, end - start + 1)

        return max_fruits
