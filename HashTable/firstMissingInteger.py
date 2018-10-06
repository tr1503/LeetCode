class Solution(object):
    def firstMissingPositive(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        m = set(nums)
        i = 1
        while i in m:
            i += 1
        return i
