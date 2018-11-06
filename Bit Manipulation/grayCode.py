class Solution:
    def grayCode(self, n):
        """
        :type n: int
        :rtype: List[int]
        """
        res = []
        for i in range(2**n):
            res.append((i >> 1) ^ i)
        return res
