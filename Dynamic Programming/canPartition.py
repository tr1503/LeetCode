# Use dynamic programming to solve this problem, the status formula is dp[j] = dp[j] or dp[j-nums[i]]
class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        s = sum(nums)
        if s % 2 != 0:
            return False
        target = s // 2
        if target in nums:
            return True
        dp = [0 for _ in range(s + 1)]
        dp[0] = 1
        for num in nums:
            for i in range(s, -1, -1):
                if dp[i]:
                    dp[i + num]  = 1
            if dp[target]:
                return True
        return False
