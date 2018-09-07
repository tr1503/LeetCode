'''Iter each row's first element and compare to target. 
If the first element is larger than target, the target must be at the last line.
If there is only one row in matrix, search that row. 
If the last row's first element is still smaller than target, search the last row.'''
class Solution(object):
    def searchMatrix(self, matrix, target):
        """
        :type matrix: List[List[int]]
        :type target: int
        :rtype: bool
        """
        if len(matrix) == 0 or len(matrix[0]) == 0:
            return False
        key = 0
        for i in range(len(matrix)):
            if target == matrix[i][0]:
                return True
            if target < matrix[i][0]:
                key = i - 1
                break
        if target in matrix[key]:
            return True
        elif target in matrix[i]:
            return True
        return False
