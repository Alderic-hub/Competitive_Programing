class Solution(object):
    def maxSlidingWindow(self, nums, k):
        ans = []
        arr = deque()
        
        for n in range(len(nums)):
            
            while arr and arr[0] <= n - k:
                arr.popleft()

            while arr and nums[arr[-1]] < nums[n]:
                arr.pop()
            arr.append(n)
            if n >= k - 1:
                ans.append(nums[arr[0]])
        
        return ans
