class Solution:
    def isInterleave(self, s1: str, s2: str, s3: str) -> bool:
        if len(s1) + len(s2) != len(s3):
            return False
        n1 = len(s1)
        n2 = len(s2)
        dp = [[False for _ in range(n2+1)] for _ in range(n1+1)]
        dp[0][0] = True
        for i in range(1, n1+1):
            if dp[i-1][0] and s1[i-1] == s3[i-1]:
                dp[i][0] = True
            else:
                dp[i][0] = False
        for i in range(1, n2+1):
            if dp[0][i-1] and s2[i-1] == s3[i-1]:
                dp[0][i] = True
            else:
                dp[0][i] = False
        for i in range(1, n1+1):
            for j in range(1, n2+1):
                if (dp[i-1][j] and s1[i-1] == s3[i-1+j]) or (dp[i][j-1] and s2[j-1] == s3[j-1+i]):
                    dp[i][j] = True
                else:
                    dp[i][j] = False
        return dp[-1][-1]
