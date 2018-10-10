#Use DP to check [0:i] and [0:j] are same for array A and B
class Solution(object):
    def findLength(self, A, B):
        """
        :type A: List[int]
        :type B: List[int]
        :rtype: int
        """
        res = 0
        dp = [[0 for _ in range(len(B)+1)] for _ in range(len(A)+1)]
        for i in range(1,len(dp)):
            for j in range(1,len(dp[i])):
                if A[i-1] == B[j-1]:
                    dp[i][j] = dp[i-1][j-1] + 1
                else:
                    dp[i][j] = 0
                res = max(res,dp[i][j])
        return res
