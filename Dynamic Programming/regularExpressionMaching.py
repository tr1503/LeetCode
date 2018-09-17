'''Use Dynamic Programming to store the matching result dp[i][j] = if s(0,i] and p(0,j] are matching.
Use this website: http://jianlu.github.io/2016/11/07/leetcode10-Regular-Expression-Matching/'''
class Solution(object):
    def isMatch(self, s, p):
        """
        :type s: str
        :type p: str
        :rtype: bool
        """
        if len(s) == 0 and len(p) == 0:
            return True
        if len(p) == 0:
            return False
        
        dp = [[False for _ in range(len(p) + 1)] for _ in range(len(s) + 1)]
        dp[0][0] = True
        for j in range(2,len(p)+1):
            if p[j-1] == '*':
                dp[0][j] = dp[0][j-2]
                
        for i in range(1,len(s) + 1):
            for j in range(1,len(p) + 1):
                if p[j-1] == '.' :
                    dp[i][j] = dp[i-1][j-1]
                elif p[j-1] == '*':
                    if dp[i][j-2] or dp[i][j-1] or ((p[j-2] == '.' or p[j-2] == s[i-1]) and dp[i-1][j]):
                        dp[i][j] = True
                else:
                    dp[i][j] = dp[i-1][j-1] and p[j-1] == s[i-1]
        
        return dp[len(s)][len(p)]
