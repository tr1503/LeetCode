class Solution(object):
    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        """
        res = 0 
        p = x
        while p > 0:
            #Reverse number formula
            res = res * 10 + p % 10
            p = p // 10
        return x == res
