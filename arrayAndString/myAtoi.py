import re
class Solution(object):
    def myAtoi(self, str):
        """
        :type str: str
        :rtype: int
        """
        m = re.search(r'^\s*([\+\-]?\d+)',str)
        if m:
            res = int(m.group(1))
            lim = 2**31
            if res < -lim:
                return -lim
            if res > lim - 1:
                return lim - 1
            return res
        return 0
