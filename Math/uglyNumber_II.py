# Because each ugly number is calculated from a previous ugly number mutiple 2, 3 or 5
# We get the minimum number from these three calculated numbers then add it to the sequence
class Solution:    
    def nthUglyNumber(self, n):
        """
        :type n: int
        :rtype: int
        """
        res = [1]
        i2 = 0
        i3 = 0
        i5 = 0
        while len(res) < n:
            m2 = res[i2] * 2
            m3 = res[i3] * 3
            m5 = res[i5] * 5
            m = min(m2, m3, m5)
            if m == m2:
                i2 += 1
            if m == m3:
                i3 += 1
            if m == m5:
                i5 += 1
            res.append(m)
        return res[-1]
