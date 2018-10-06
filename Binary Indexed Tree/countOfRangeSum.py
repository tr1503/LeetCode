'''Use Binary Indexed Tree to get the number of each value in array which is in the interval
[lower + sum[i-1], upper + sum[i-1]]. 
Firstly, build a binary indexed tree. 
Then, iter from right to left, use binary indexed tree to get the sums of all numbers smaller than each value.
Finally, update them.'''
class BinaryIndexTree(object):
    def __init__(self, n):
        self.sums = [0 for _ in range(n+1)]
        self.n = n
    def lowbit(self, x):
        return x & -x
    def add(self, x, val):
        while x <= self.n:
            self.sums[x] += val
            x += self.lowbit(x)
    def sum(self, x):
        res = 0
        while x > 0:
            res += self.sums[x]
            x -= self.lowbit(x)
        return res
    
class Solution(object):
    def countRangeSum(self, nums, lower, upper):
        """
        :type nums: List[int]
        :type lower: int
        :type upper: int
        :rtype: int
        """
        if not nums:
            return 0
        sums = [upper, lower - 1]
        total = 0
        for num in nums:
            total += num
            sums += [total, total + lower - 1, total + upper]
        index = {}
        for i, x in enumerate(sorted(set(sums))):
            index[x] = i + 1
        bit = BinaryIndexTree(len(index))
        ans = 0
        for i in range(len(nums) - 1, -1, -1):
            bit.add(index[total],1)
            total -= nums[i]
            ans += bit.sum(index[upper+total]) - bit.sum(index[lower+total-1])
        return ans
