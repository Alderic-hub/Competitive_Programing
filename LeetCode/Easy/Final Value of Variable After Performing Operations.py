class Solution(object):
    def finalValueAfterOperations(self, operations):
        val = 0
        for items in operations:
            if items in ["X++","++X"]:
                val += 1
            else:
                val -= 1
        return val
