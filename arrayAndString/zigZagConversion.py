class Solution(object):
    def convert(self, s, numRows):
        """
        :type s: str
        :type numRows: int
        :rtype: str
        """
        if numRows < 2:
            return s
        inc = (numRows - 1) * 2 #Initialize inc
        res = ""
        for i in range(numRows):
            j = i
            d1 = (numRows - i - 1) * 2
            while j < len(s):
                res += s[j]
                if d1 != 0 and d1 != inc and j + d1 < len(s):
                    res += s[j+d1]
                j += inc
        return res
