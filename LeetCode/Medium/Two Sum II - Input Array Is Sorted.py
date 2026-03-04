class Solution(object):
    def twoSum(self, numbers, target):
        num = 1
        length = len(numbers)
        while num <= length:
            sum = numbers[num-1]+numbers[length-1]
            if sum < target:
                num += 1
            elif sum > target:
                length -= 1
            else:
                ans=[num,length]
                break
        return ans

        
