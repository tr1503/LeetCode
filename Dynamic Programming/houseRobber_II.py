'''Use Dynamic Programming to get the max sums between 0 to last - 1 and between 1 to last.
The result is max of these two. It needs O(4n) time, should be reduced.'''
class Solution(object):
    def rob(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if not nums:
            return 0
        if len(nums) == 1:
            return nums[0]
        sums1 = [0 for _ in range(len(nums))]
        sums2 = [0 for _ in range(len(nums))]
        for i in range(len(sums1) - 1):
            if i == 0:
                sums1[i] = nums[i]
            elif i == 1:
                sums1[i] = max(nums[i],nums[i-1])
            else:
                sums1[i] = max(sums1[i-2] + nums[i], sums1[i-1])
        ans1 = sums1[len(sums1) - 2]
        for i in range(1,len(sums2)):
            if i == 1:
                sums2[i] = nums[i]
            elif i == 2:
                sums2[i] = max(nums[i],nums[i-1])
            else:
                sums2[i] = max(sums2[i-2] + nums[i], sums2[i-1])
        ans2 = sums2[len(sums2) - 1]
        return max(ans1,ans2)
