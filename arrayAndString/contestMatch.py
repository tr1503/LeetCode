class Solution:
    def findContestMatch(self, n):
        """
        :type n: int
        :rtype: str
        """
        res = []
        for i in range(1,n+1):
            res.append(str(i))
        
        def helper(n,res):
            if n == 1:
                return
            for i in range(n):
                res[i] = "(" + res[i] + "," + res[n - i - 1] + ")"
            helper(n // 2,res)
        helper(n,res)
        return res[0]
