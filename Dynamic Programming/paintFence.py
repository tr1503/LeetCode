'''If n = 1, there are k ways. If n >= 2 and k >= 2, there are two ways for one fence:
One is same as the last one, one is different. If we use different color, it should have k-1 ways.
If we use same color, the number of ways should be same as the last fence's number of ways.'''
class Solution(object):
    def numWays(self, n, k):
        """
        :type n: int
        :type k: int
        :rtype: int
        """
        if n == 0:
            return 0
        same, diff = 0, k
        for i in range(2,n+1):
            temp = diff
            diff = (same + diff) * (k - 1)
            same = temp
        return same + diff
