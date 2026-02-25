class Solution(object):
    def findDiagonalOrder(self, mat):
        row_max = len(mat)
        col_max = len(mat[0]) 
        row = 0
        col = 0
        ans = []
        total = len(mat) * len(mat[0])
        Truth = True
        while Truth:
            while row > -1 and col < col_max:
                ans.append(mat[row][col])
                row -=1
                col +=1
            if col >= col_max:
                row += 2
                col -=1
            else:
                if row == -1:
                    row += 1
            if len(ans) == total:
                break
            while row < row_max and col > -1:
                ans.append(mat[row][col])
                col -= 1
                row += 1
            if row >= row_max:
                row -= 1
                col += 2
            else:
                if col == -1:
                    col += 1
            if len(ans) == total:
                break
        return ans
            
                    

        
