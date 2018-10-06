class Solution(object):
    def findMaxConsecutiveOnes(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        res = nums[0]
        origin = nums[0]
        for i in range(1,len(nums)):
            if origin == origin + nums[i]:
                res = max(res, origin)
                origin = 0
            else:
                origin = origin + nums[i]
        res = max(res,origin)
        return res
