# Happy number should not have 4 in iteration
class Solution(object):
    def isHappy(self, n):
        """
        :type n: int
        :rtype: bool
        """
        while n != 1 and n != 4:
            t = 0
            while n:
                t += (n % 10) * (n % 10)
                n /= 10
            n = t
        return n == 1
