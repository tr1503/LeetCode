class Solution:
    def searchInsert(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        if target < nums[0]:
            return 0
        if target > nums[-1]:
            return len(nums)
        lo = 0
        hi = len(nums) - 1
        while lo + 1 < hi:
            mid = lo + (hi - lo) // 2
            if nums[mid] == target:
                return mid
            elif nums[mid] < target:
                lo = mid
            else:
                hi = mid
        if target <= nums[lo]:
            return lo
        elif target <= nums[hi]:
            return hi
        else:
            return hi
