class Solution:
    def countPrimes(self, n):
        """
        :type n: int
        :rtype: int
        """
        if n == 0 or n == 1:
            return 0
        num = [True] * (n - 1)
        num[0] = False
        res = 0
        limit = int(math.sqrt(n))
        for i in range(2, limit + 1):
            if num[i-1]:
                for j in range(i*i, n, i):
                    num[j-1] = False
        for j in range(n-1):
            if num[j]:
                res += 1
        return res
