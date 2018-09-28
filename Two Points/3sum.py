'''Sort the array firstly and use two pointers to track from left to right.
If nums[i] + nums[left] + nums[right] == 0, add them to the result.
But we need to prevent the repeated situation. There are three situations can cause repeat:
1) i>0 and nums[i] == nums[i-1], we should skip this iter.
2) left < right and nums[left] == nums[left-1] after left += 1, we should get the next iter value.
3) left < right and nums[right] == nums[right+1], same as second situation.'''
class Solution(object):
    def threeSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        if len(nums) < 3:
            return []
        res = []
        nums.sort()
        for i in range(len(nums) - 2):
            if i > 0 and nums[i] == nums[i-1]:
                continue
            left = i + 1
            right = len(nums) - 1
            while left < right:
                s = nums[i] + nums[left] + nums[right]
                if s == 0:
                    res.append([nums[i],nums[left],nums[right]])
                    left += 1
                    right -= 1
                    while left < right and nums[left] == nums[left-1]:
                        left += 1
                    while left < right and nums[right] == nums[right+1]:
                        right -= 1
                elif s < 0:
                    left += 1
                else:
                    right -= 1
        return res
