class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        myDict = {}
        for i in range(len(nums)):
            if nums[i] in myDict:
                return myDict[nums[i]],i
            myDict[target - nums[i]] = i
        return -1
