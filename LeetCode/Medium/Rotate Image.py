class Solution(object):
    def rotate(self, matrix):
        length = len(matrix)
        row = len(matrix[0])
        column = len(matrix) 
        for r in range(row):
            val = []
            c = column -1
            while c >= 0:
                val.append(matrix[c][r])
                c -= 1
            matrix.append(val)
        for i in range(column):
            matrix.pop(0)

        
