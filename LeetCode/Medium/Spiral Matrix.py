class Solution(object):
    def spiralOrder(self, matrix):
        colS = 0
        colE = len(matrix[0]) - 1
        rowE = len(matrix) - 1
        rowS = 0
        val = 1
        ans = []
        Truth = True
        while Truth:
            for n in range(colS, colE+1,val):
                ans.append(matrix[rowS][n])
            rowS += 1
            if rowE < rowS or colS > colE:
                Truth = False
                break
            for n in range(rowS, rowE+1, val):
                ans.append(matrix[n][colE])
            colE -= 1
            val = -1
            if rowE < rowS or colS > colE:
                Truth = False
                break
            for n in range(colE, colS-1,val):
                ans.append(matrix[rowE][n])
            rowE -= 1
            if rowE < rowS or colS > colE:
                Truth = False
                break
            for n in range(rowE, rowS-1, val):
                ans.append(matrix[n][colS])
            colS += 1
            val = 1
            if rowE < rowS or colS > colE:
                Truth = False
                break
        return ans
               
