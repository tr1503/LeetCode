# set each element i of its nums[nums[i] - 1] to negative number
# then the next duplicate number will meet the negative and add it to result
class Solution:
    def findDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        res = []
        for i in range(len(nums)):
            index = abs(nums[i]) - 1
            if (nums[index] < 0):
                res.append(index + 1)
            nums[index] = -nums[index]
        return res
