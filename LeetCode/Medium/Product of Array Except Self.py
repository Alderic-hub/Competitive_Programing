class Solution(object):
    def productExceptSelf(self, nums):
        length = len(nums)
        left_ans = list()
        right_ans = list()
        answer = list()
        
        for n in range(length):
            if n == 0:
                left_ans.append(1)
            else:
                left_ans.append(nums[n-1] * left_ans[-1])
        
        for n in range(length-1, -1, -1):
            if n == length - 1:
                right_ans.append(1)
            else:
                right_ans.append(nums[n+1] * right_ans[-1])
        
        right_ans.reverse()
        
        for n in range(length):
            answer.append(left_ans[n] * right_ans[n])
        
        return answer
