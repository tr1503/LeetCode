'''Use dynamic programming to convert this question to fib iter solution.'''
class Solution:
    def climbStairs(self, n):
        """
        :type n: int
        :rtype: int
        """
        time = [0 for _ in range(n+1)]
        time[0] = 1
        time[1] = 1
        for i in range(2, n+1, 1):
            time[i] = time[i-1] + time[i-2]
        
        return time[n]
