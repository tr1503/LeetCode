class Solution(object):
    def myPow(self, x, n):
        """
        :type x: float
        :type n: int
        :rtype: float
        """
        if n < 0:
            x = 1 / x
            n = -n
        ans = 1
        product = x
        i = n
        #The way here is like: 36 = 2*((2*2)*(2*2))
        while i > 0:
            if i % 2 == 1:
                ans = ans * product
            product = product * product
            i /= 2
        return ans
