class Solution(object):
    def evalRPN(self, tokens):
        nums = []
        operators = ['/', '+', '-','*']
        for items in tokens:
            if items not in operators:
                nums.append(int(items))
            else:
                val1 = nums.pop()
                val2 = nums.pop()
                if items == '+':
                    nums.append(val1+val2)
                elif items == '-':
                    nums.append(val2-val1)
                elif items == '*':
                    nums.append(val2*val1)
                else:
                    val = float(val2)/val1
                    val = int(val)   
                    nums.append(val)
        return nums[0]

         

        
