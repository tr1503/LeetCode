'''Use Dynamic Programming to get the state and state function:
   new state max amount P[i] = max(nums[i] + P[i-2],P[i-1]).'''
class Solution(object):
    def rob(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if not nums:
            return 0
        sums = [0 for _ in range(len(nums))]
        for i in range(len(sums)):
            if i == 0:
                sums[i] = nums[i]
            elif i == 1:
                sums[i] = max(nums[i],nums[i-1])
            else:
                sums[i] = max(nums[i] + sums[i-2], sums[i-1])
        return sums[len(sums) - 1]
