class Solution(object):
    def transpose(self, matrix):
        ans = []
        count = -1
        length = len(matrix[0])
        amount = len(matrix)
        for _ in range(length):
            ans_list = []
            count += 1
            for items in matrix:
                ans_list.append(items[count])
            ans.append(ans_list)
        return ans


        
