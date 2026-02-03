class Solution(object):
    def fizzBuzz(self, n):
        ans = []
        for items in range(1,n+1):
            if items%3 == 0:
                if items%5 == 0:
                    ans.append("FizzBuzz")
                else:
                    ans.append("Fizz")
            elif items%5 == 0:
                ans.append("Buzz")
            else:
                ans.append(str(items))
        return ans
