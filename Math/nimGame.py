class Solution:
    def canWinNim(self, n):
        """
        :type n: int
        :rtype: bool
        """
        return n & 3 != 0
