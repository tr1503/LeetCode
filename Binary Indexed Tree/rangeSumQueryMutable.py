'''Use binary indexed tree to solve this problem. 
Time is O(nlogn). Try to figure out it by Google angin.'''
class NumArray(object):

    def __init__(self, nums):
        """
        :type nums: List[int]
        """
        self._sums = [0 for _ in range(len(nums) + 1)]
        self.size = len(nums)
        self.nums = nums
        for i in range(len(nums)):
            self.add(i + 1, nums[i])

    def add(self, i, delta):
        while i <= self.size:
            self._sums[i] += delta
            i += i & -i
    
    def sum(self, i):
        s = 0
        while i > 0:
            s += self._sums[i]
            i -= i & -i
        return s
    
    def update(self, i, val):
        """
        :type i: int
        :type val: int
        :rtype: void
        """
        self.add(i + 1, val - self.nums[i])
        self.nums[i] = val
    
    def sumRange(self, i, j):
        """
        :type i: int
        :type j: int
        :rtype: int
        """
        if len(self.nums) == 0:
            return 0
        return self.sum(j + 1) - self.sum(i)
        


# Your NumArray object will be instantiated and called as such:
# obj = NumArray(nums)
# obj.update(i,val)
# param_2 = obj.sumRange(i,j)
