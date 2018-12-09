# Use binary search to solve this problem from the left upper conner to right buttom conner
# time is O(nlogX), x is the diff between max value and min value
class Solution:
    def search(self, matrix, target):
        n = len(matrix)
        i = n - 1
        j = 0
        res = 0
        while i >= 0 and j < n:
            if matrix[i][j] <= target:
                res +=  i + 1
                j += 1
            else:
                i -= 1
        return res
    
    def kthSmallest(self, matrix, k):
        """
        :type matrix: List[List[int]]
        :type k: int
        :rtype: int
        """
        left = matrix[0][0] 
        right = matrix[-1][-1]
        while left < right:
            mid = left + (right - left) // 2
            count = self.search(matrix, mid)
            if count < k:
                left = mid + 1
            else:
                right = mid
        return left
