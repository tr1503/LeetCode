class Solution(object):
    def moveZeroes(self, nums):
        """
        :type nums: List[int]
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        n = len(nums)
        left = 0
        right = 1
        move_l = True
        #Move the zero one by one by two pointers
        while left < n and right < n:
            if nums[right] == 0:
                right += 1
            elif nums[left] == 0:
                temp = nums[left]
                nums[left] = nums[right]
                nums[right] = temp
                left += 1
            else:
                if move_l:
                    left += 1
                else:
                    right += 1
                move_l = not move_l
