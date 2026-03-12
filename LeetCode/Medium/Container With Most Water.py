class Solution(object):
    def maxArea(self, height):

        end = len(height)-1
        start = 0
        distance = len(height)-1
        arr = []
        while start < end:
            small = min(height[start],height[end])
            area = small * distance
            arr.append(area)
            if small == height[start]:
                start += 1
            else:
                end -= 1
            distance -= 1
        ans = max(arr)
        return ans

