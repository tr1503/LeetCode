'''Use a similar way as Fib. Check the last value in string. 
If the last value is 0, the decode ways at this value should be 0.
Otherwise the dp value should add dp[i-1]. 
If the position is not at beginning and the combination of last two values are smaller than
26 and larger than 10, add dp[i-2].'''
class Solution(object):
    def numDecodings(self, s):
        """
        :type s: str
        :rtype: int
        """
        '''if not s or s[0] == "0":
            return 0
        dp = [0 for _ in range(len(s) + 1)]
        dp[0] = 1
        for i in range(1,len(dp)):
            if s[i-1] == '0':
                dp[i] = 0
            else:
                dp[i] = dp[i-1]
            if i > 1 and (s[i - 2] == '1' or (s[i-2] == '2' and s[i-1] <= '6')):
                dp[i] += dp[i-2]
        return dp[len(dp) - 1]'''
        if not s or s[0] == '0':
            return 0
        c1 = 1
        c2 = 1
        for i in range(1,len(s)):
            if s[i] == '0':
                c1 = 0
            if s[i-1] == '1' or (s[i-1] == '2' and s[i] <= '6'):
                c1 = c1 + c2
                c2 = c1 - c2
            else:
                c2 = c1
        return c1
