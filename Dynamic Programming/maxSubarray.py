'''Iter the original array to have a new array to store the maximum between the last start value + this value and this value. 
If this value is larger than itself + the last start value, reset this value as a new start value. 
Pick the max start value to end value.'''

class Solution:
    def maxSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        p = [0 for _ in range(len(nums))]
        p[0] = nums[0]
        for i in range(1, len(nums), 1):
            p[i] = max(p[i-1] + nums[i], nums[i])
        return max(p)
