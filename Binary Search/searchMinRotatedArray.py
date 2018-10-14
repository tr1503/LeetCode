class Solution:
    def findMin(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        def helper(nums,lo,hi):
            #Only 1 or 2 elements in this array
            if lo + 1 >= hi:
                return min(nums[lo],nums[hi])
            #Sorted Array
            if nums[lo] < nums[hi]:
                return nums[lo]
            mid = lo + (hi - lo) // 2
            return min(helper(nums,lo,mid-1),helper(nums,mid,hi))
        return helper(nums,0,len(nums)-1)
