class Solution(object):
    def findDisappearedNumbers(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        res = []
        for i in range(len(nums)):
            m = abs(nums[i]) - 1
            if nums[m] > 0:
                nums[m] = -nums[m]
            else:
                nums[m] = nums[m]
        for i in range(len(nums)):
            if nums[i] > 0:
                res.append(i + 1)
        return res
