# Use exclusive or to get the possible duplicated position
# Use binary search to get the single element
class Solution:
    def singleNonDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        lo = 0
        hi = len(nums) - 1
        while lo < hi:
            mid = lo + (hi - lo) // 2
            # mid = mid + 1 if mid % 2 == 0 else mid - 1
            n = mid ^ 1
            # before position n are duplicated, the result must be on the right side
            if nums[n] == nums[mid]:
                lo = mid + 1
            else:
                hi = mid
        return nums[lo]
