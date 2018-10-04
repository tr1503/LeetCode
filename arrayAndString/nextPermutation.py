'''Firstly, iter from tail to head and get the first number which is smaller than its right number.
Then, iter from tail again to get the first number which is larger than the first number we get.
Swap them. Finally, get reverse whole list from the tail to the first number.'''
class Solution(object):
    def nextPermutation(self, nums):
        """
        :type nums: List[int]
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        i = len(nums) - 2
        while i >= 0 and nums[i] >= nums[i+1]:
            i -= 1
        if i >= 0:
            j = len(nums) - 1
            while j >= 0 and nums[j] <= nums[i]:
                j -= 1
            temp = nums[i]
            nums[i] = nums[j]
            nums[j] = temp
        i += 1
        k = len(nums) - 1
        while i < k:
            temp = nums[i]
            nums[i] = nums[k]
            nums[k] = temp
            i += 1
            k -= 1
