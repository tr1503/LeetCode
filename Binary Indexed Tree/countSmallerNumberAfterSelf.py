'''Use Binary Indexed Tree to convert the question to get the sum of interval question.'''
class BITree(object):
    def __init__(self, n) :
        self._sums = [0 for _ in range(n+1)]
    
    def update(self, i, delta):
        while i < len(self._sums):
            #Update by the sum
            #Use bitcode to add
            self._sums[i] += delta
            i += i & -i
    
    def query(self, i):
        s = 0
        while i > 0:
            #Query from the leaf to root
            #Use bitcode to get root, the root must be 2^n
            s += self._sums[i]
            i -= i & -i
        return s
    
class Solution(object):
    def countSmaller(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        sortNums = sorted(set(nums))
        ranks = {}
        #Get each number's rank
        for i in range(len(sortNums)):
            ranks[sortNums[i]] = i + 1  
        ans = []
        bitree = BITree(len(ranks))
        i = len(nums) - 1
        while i >= 0:
            #Get the freq of the number which smaller than this number
            ans.append(bitree.query(ranks[nums[i]] - 1))
            #Add the rank of number to bit. The sum is one.
            bitree.update(ranks[nums[i]], 1)
            i-= 1
        return list(reversed(ans))
