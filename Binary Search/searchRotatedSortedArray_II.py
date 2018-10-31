class Solution:
    def search(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: bool
        """
        if not nums:
            return False
        lo = 0
        hi = len(nums) - 1
        while lo + 1 < hi:
            mid = lo + (hi - lo) // 2
            if nums[mid] == target:
                return True
            if nums[lo] == nums[mid] and nums[mid] == nums[hi]:
                lo += 1
                hi -= 1
            elif nums[lo] <= nums[mid]:
                if nums[lo] <= target and target <= nums[mid]:
                    hi = mid
                else:
                    lo = mid
            else:
                if nums[mid] <= target and target <= nums[hi]:
                    lo = mid
                else:
                    hi = mid
        if nums[lo] == target:
            return True
        if nums[hi] == target:
            return True
        return False
