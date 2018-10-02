class Solution(object):
    def PredictTheWinner(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        def canWin(nums, s, e, dp):
            if dp[s][e] == -1:
                if s == e:
                    #Only one number
                    dp[s][e] = nums[s]
                else:
                    #Two situation: pick first value or last value. Get the current sum for player1
                    dp[s][e] = max(nums[s] - canWin(nums,s+1,e,dp), nums[e] - canWin(nums,s,e-1,dp))
            return dp[s][e]
        n = len(nums)
        dp = [[-1 for _ in range (n)] for _ in range(n)]
        return canWin(nums,0,n-1,dp) >= 0
