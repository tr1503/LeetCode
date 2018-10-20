class Solution:

    def __init__(self, w):
        """
        :type w: List[int]
        """
        self.length = len(w)
        self.presum = [0] * self.length
        self.total = 0
        for i in range(self.length):
            self.total += w[i]
            self.presum[i] = self.total
    
    def binarySearch(self, target):
        lo = 0
        hi = self.length
        while lo < hi:
            mid = (lo + hi) // 2
            if self.presum[mid] == target:
                return mid
            elif self.presum[mid] < target:
                lo = mid + 1
            else:
                hi = mid
        return lo
    
    def pickIndex(self):
        """
        :rtype: int
        """
        rand = random.uniform(0,self.total)
        return self.binarySearch(rand)


# Your Solution object will be instantiated and called as such:
# obj = Solution(w)
# param_1 = obj.pickIndex()
