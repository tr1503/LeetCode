class Solution:
    def productExceptSelf(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        #Create a new array
        res = [1 for _ in range(len(nums))]
        prev = 1
        #Multiple each number with last number's product from left to right
        for i in range(len(nums)):
            res[i] *= prev
            prev *= nums[i]
        future = 1
        #Multiple each number with next number's product from right to left
        for i in range(len(nums)-1,-1,-1):
            res[i] *= future
            future *= nums[i]
        return res
