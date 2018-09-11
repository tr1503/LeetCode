'''Use Binary Indexed Tree to solve this question. 
The method is from http://bookshadow.com/weblog/2017/02/12/leetcode-reverse-pairs/'''
class BITree(object):
    def __init__(self,n):
        self._sums = [0 for _ in range(n + 1)]
    
    def update(self, i, delta):
        while i < len(self._sums):
            self._sums[i] += delta
            i += i & -i
            
    def query(self, i):
        s = 0
        while i > 0:
            s += self._sums[i]
            i -= i & -i
        return s
    
class Solution(object):
    def reversePairs(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        ans = 0
        nums2 = [n * 2 for n in nums]
        sortNums = sorted(set(nums + nums2))
        pairs = {}
        for i in range(len(sortNums)):
            pairs[sortNums[i]] = i + 1
        bitree = BITree(len(pairs))
        i = len(nums) - 1
        while i >= 0:
            ans += bitree.query(pairs[nums2[i] / 2] - 1)
            bitree.update(pairs[nums2[i]], 1)
            i -= 1
        return ans
