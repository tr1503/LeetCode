'''Start from the right coner of matrix. 
If it is larger than target, iter this row from here to start.
If it is smaller than target, iter this col from here to end.'''
class Solution(object):
    def searchMatrix(self, matrix, target):
        """
        :type matrix: List[List[int]]
        :type target: int
        :rtype: bool
        """
        if len(matrix) == 0 or len(matrix[0]) == 0:
            return False
        j, i = len(matrix[0]) - 1, 0
        while j >= 0 and i <= len(matrix) - 1:
            if matrix[i][j] == target:
                return True
            elif matrix[i][j] < target:
                i += 1
            elif matrix[i][j] > target:
                j -= 1
                
        return False
