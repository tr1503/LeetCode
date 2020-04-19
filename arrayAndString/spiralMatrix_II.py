class Solution:
    def generateMatrix(self, n: int) -> List[List[int]]:
        matrix = []
        for i in range(n):
            matrix.append([0 for _ in range(n)])
        
        num = 1
        colBegin = 0
        colEnd = n - 1
        rowBegin = 0
        rowEnd = n - 1
        while colBegin <= colEnd and rowBegin <= rowEnd:
            for i in range(colBegin, colEnd + 1):
                matrix[rowBegin][i] = num
                num += 1
            rowBegin += 1
            
            for i in range(rowBegin, rowEnd + 1):
                matrix[i][colEnd] = num
                num += 1
            colEnd -= 1
            
            if rowBegin <= rowEnd:
                for i in range(colEnd, colBegin - 1, -1):
                    matrix[rowEnd][i] = num
                    num += 1
                rowEnd -= 1
            
            if colBegin <= colEnd:
                for i in range(rowEnd, rowBegin - 1, -1):
                    matrix[i][colBegin] = num
                    num += 1
                colBegin += 1
        return matrix
