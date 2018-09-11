'''Use Dynamic Programming to get each sum before this index, so we don't need to add to the sum repeatedly.
Each sum = this number + the sum of this index. 
The result should be index j+1 - index i.'''
class NumArray(object):

    def __init__(self, nums):
        """
        :type nums: List[int]
        """
        self.nums = nums
        self._sums = [0 for _ in range(len(nums) + 1)]
        for i in range(len(nums)):
            self._sums[i + 1] = nums[i] + self._sums[i]

    def sumRange(self, i, j):
        """
        :type i: int
        :type j: int
        :rtype: int
        """
        return self._sums[j+1] - self._sums[i]


# Your NumArray object will be instantiated and called as such:
# obj = NumArray(nums)
# param_1 = obj.sumRange(i,j)
