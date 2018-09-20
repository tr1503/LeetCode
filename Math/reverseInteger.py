class Solution(object):
    def reverse(self, x):
        """
        :type x: int
        :rtype: int
        """
        res = 0
        check = x
        origin = abs(x)
        x = abs(x)
        flag = len(str(x)) - 1
        while x > 0:
            if x % 10 == 0 and x == origin:
                flag -= 1
                x = x // 10
                continue
            else:
                res += x % 10 * (10 ** flag)
                flag -= 1
                x = x // 10
        if res > (2 ** 31) - 1 or res < -(2 ** 31):
            return 0
        if check > 0:
            return res
        else:
            return -res
