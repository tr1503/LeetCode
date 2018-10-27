class Solution(object):
    def threeSumClosest(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        res = nums[0] + nums[1] + nums[-1]
        nums.sort()
        for i in range(len(nums) - 2):
            left = i + 1
            right = len(nums) - 1
            while left < right:
                s = nums[i] + nums[left] + nums[right]
                if s > target:
                    right -= 1
                else:
                    left += 1
                if abs(s - target) < abs(res - target):
                    res = s
        return res
