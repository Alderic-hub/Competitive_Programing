class NumArray(object):

    def __init__(self, nums):        
        self.sum_vals = []
        val = 0
        for n in nums:
            val+=n
            self.sum_vals.append(val)
        

    def sumRange(self, left, right):
        if left > 0:
            value = self.sum_vals[right]-self.sum_vals[left-1]
        else:
            value = self.sum_vals[right]

        return value
    
        


# Your NumArray object will be instantiated and called as such:
# obj = NumArray(nums)
# param_1 = obj.sumRange(left,right)
