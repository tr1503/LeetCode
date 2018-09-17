'''Use dynamic programming to create an array to use repeatly from the bottom to top.
The min value in dp is the small number between this value and last value + the value itself.'''
class Solution(object):
    def minimumTotal(self, triangle):
        """
        :type triangle: List[List[int]]
        :rtype: int
        """
        if not triangle:
            return 0
        dp = [0 for _ in range(len(triangle))]
        i = len(triangle) - 1
        while i >= 0:
            for j in range(len(triangle[i])):
                if i == len(triangle) - 1:
                    dp[j] = triangle[i][j]
                else:
                    dp[j] = min(dp[j],dp[j+1]) + triangle[i][j]
            i-=1
        return dp[0]
