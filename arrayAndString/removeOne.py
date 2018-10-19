class Solution:
    """
    @param matrix: 
    @param x: 
    @param y: 
    @return: return the matrix
    """
    def removeOne(self, matrix, x, y):
        for i in range(x,len(matrix)):
            matrix[i][y] = 0
        return matrix
