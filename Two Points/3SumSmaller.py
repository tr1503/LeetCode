'''Convert this question from 3Sum to 2Sum, and use two pointers to get 2Sums
smaller than target. And Use 2Sum again to iter numbers to get 2Sum of values and their diff with target.'''
class Solution(object):
    def twoSumSmaller(self, nums, start, target):
        res = 0
        left = start
        right = len(nums) - 1
        while left < right:
            if nums[left] + nums[right] < target:
                res += right - left
                left += 1
            else:
                right -= 1
        return res
    
    def threeSumSmaller(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        nums.sort()
        res = 0
        for i in range(len(nums) - 2):
            res += self.twoSumSmaller(nums,i + 1,target - nums[i])
        return res
