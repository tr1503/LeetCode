# Same as 153, when the left element, right element and middle element are same,
# the binary search will fail. So we need to move left element to right.
# The time is O(n) when all numbers are duplicated. 
class Solution:
    def findMin(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if not nums:
            return 0
        left = 0
        right = len(nums) - 1
        res = nums[0]
        while left < right - 1:
            mid = left + (right - left) // 2
            if nums[left] < nums[mid]:
                res = min(res, nums[left])
                left = mid + 1
            elif nums[left] > nums[mid]:
                res = min(res, nums[right])
                right = mid
            else:
                left += 1
        res = min(res, nums[left])
        res = min(res, nums[right])
        return res
