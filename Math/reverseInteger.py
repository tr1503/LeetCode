class Solution(object):
    def reverse(self, x):
        """
        :type x: int
        :rtype: int
        """
        res = 0
        origin = x
        x = abs(x)
        flag = len(str(x)) - 1
        while x > 0:
            res += x % 10 * (10 ** flag)
            flag -= 1
            x = x // 10
        if res > (2 ** 31) - 1 or res < -(2 ** 31):
            return 0
        if origin > 0:
            return res
        else:
            return -res
          
