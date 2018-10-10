class Solution(object):
    def strobogrammatic(self, n):
        res = []
        if n == 1:
            return ["0","1","8"]
        if n == 2:
            return ["00","11","69","88","96"]
        for s in self.strobogrammatic(n-2):
            res.append("0" + s + "0")
            res.append("1" + s + "1")
            res.append("6" + s + "9")
            res.append("8" + s + "8")
            res.append("9" + s + "6")
        return res
    
    def number(self, n):
        if n == 0:
            return 0
        if n % 2 == 0:
            return 4 * (5**(n/2-1))
        elif n == 1:
            return 3
        else:
            return 3 * (5**(n/2-1))*4
        
    def below(self, n, include = True):
        res = 0
        for i in range(1,len(n)):
            res += self.number(i)
        l = self.strobogrammatic(len(n))
        if include:
            l = [num for num in l if (len(num) == 1 or num[0] != '0') and num <= n]
        else:
            l = [num for num in l if (len(num) == 1 or num[0] != '0') and num < n]
        return res + len(l)
    
    def strobogrammaticInRange(self, low, high):
        """
        :type low: str
        :type high: str
        :rtype: int
        """
        a = self.below(high)
        b = self.below(low,include = False)
        return a - b if a > b else 0
