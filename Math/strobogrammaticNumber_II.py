class Solution(object):
    def findStrobogrammatic(self, n):
        """
        :type n: int
        :rtype: List[str]
        """
        one = ["0","1","8"]
        two = [""]
        res = [""]
        if n % 2 == 1:
            res = one
        for i in range((n % 2)+2,n+1,2):
            t = []
            for num in res:
                if i != n:
                    t.append("0" + num + "0")
                t.append("1" + num + "1")
                t.append("6" + num + "9")
                t.append("8" + num + "8")
                t.append("9" + num + "6")
            res = t
        return res
