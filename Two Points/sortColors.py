'''Set two pointers, one from left, another from right. 
Iter whole list, if the value is 0, swap to the left place and iter next value.
If the value is 1, stay it and iter next value.
If the value is 2, swap to the right place but do not iter to next,
cuz we do not know the number swap to this i is in right place.'''
class Solution(object):  
    def sortColors(self, nums):
        """
        :type nums: List[int]
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        red = 0
        blue = len(nums) - 1
        i = 0
        while i < blue + 1:
            if nums[i] == 0:
                temp = nums[i]
                nums[i] = nums[red]
                nums[red] = temp
                red += 1
                i += 1
            elif nums[i] == 1:
                i += 1
            elif nums[i] == 2:
                temp = nums[i]
                nums[i] = nums[blue]
                nums[blue] = temp
                blue -= 1
