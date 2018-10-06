class Solution(object):
    def firstMissingPositive(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        for i in range(len(nums)):
            if nums[i] <= 0:
                nums[i] = len(nums) + 1
        for n in nums:
            val = abs(n) - 1
            if val < len(nums) and nums[val] > 0:
                nums[val] = -nums[val]
        for j in range(len(nums)):
            if nums[j] > 0:
                return j + 1
        return len(nums) + 1
