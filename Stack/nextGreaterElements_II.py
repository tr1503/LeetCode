class Solution:
    def nextGreaterElements(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        n = len(nums)
        res = [-1] * n
        stack = []
        for i in range(2*n):
            # Use mod to get the element from array
            num = nums[i % n]
            while len(stack) != 0 and nums[stack[-1]] < num:
                res[stack[-1]] = num
                stack.pop()
            # i must be smaller than n because the i more than n is for getting the greater element
            # for the cycle array. We can't push it to stack.
            if i < n:
                stack.append(i)
        return res
