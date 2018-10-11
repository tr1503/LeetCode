class Solution:
    def canJump(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        res = 0
        for i in range(len(nums)):
            if i > res:
                return False
            res = max(res,nums[i] + i)
        return True
