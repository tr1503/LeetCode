class Solution(object):
    def hammingWeight(self, n):
        """
        :type n: int
        :rtype: int
        """
        count = 0
        while n > 0:
            r = n % 2
            n = n / 2
            if r == 1:
                count += 1
        return count
