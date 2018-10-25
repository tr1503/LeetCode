class Solution:
    def wiggleSort(self, nums):
        """
        :type nums: List[int]
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        # sort and swap between two elements, time is O(nlogn)
        '''nums.sort()
        if len(nums) <= 2:
            return
        for i in range(2,len(nums),2):
            nums[i],nums[i-1] = nums[i-1], nums[i]'''
        # odd element must >= the last element
        # even element must <= the last element
        if len(nums) <= 1:
            return
        for i in range(len(nums)):
            if (i % 2 == 0 and nums[i] > nums[i-1]) or (i % 2 == 1 and nums[i] < nums[i-1]):
                nums[i-1],nums[i] = nums[i],nums[i-1]
