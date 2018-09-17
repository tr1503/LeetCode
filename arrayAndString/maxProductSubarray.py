'''Use dynamic programming to get two dp array. One for max another for min. 
The result is the larger number between two max value in dp arrays.'''
class Solution(object):
    def maxProduct(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        dp_max = [0 for _ in range(len(nums))]
        dp_min = [0 for _ in range(len(nums))]
        dp_max[0] = nums[0]
        dp_min[0] = nums[0]
        for i in range (1,len(nums)):
            dp_max[i] = max(nums[i]*dp_max[i-1],nums[i]*dp_min[i-1],nums[i])
            dp_min[i] = min(nums[i]*dp_max[i-1],nums[i]*dp_min[i-1],nums[i])
        return max(max(dp_max),max(dp_min))
