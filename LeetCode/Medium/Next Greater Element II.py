class Solution(object):
    def nextGreaterElements(self, nums):
        ans = []
        length = len(nums)
        counter = 0
        while counter < length:
            val = nums[counter]
            pointer = counter + 1
            if pointer == length:
                pointer = 0
            truth = False
            while pointer != counter:
                if nums[pointer] > val:
                    ans.append(nums[pointer])
                    truth = True
                    break
                pointer += 1
                if pointer == length:
                    pointer = 0

            if not truth:
                ans.append(-1)
            counter += 1
        return ans
