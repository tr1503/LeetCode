class Solution(object):
    def dominantIndex(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        maximum = max(nums)
        for num in nums:
            if num * 2 > maximum and num != maximum:
                return -1
        return nums.index(maximum)
