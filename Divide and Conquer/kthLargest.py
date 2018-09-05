'''Use quick selection to partite the array to two subarrays. 
The explaination is at http://www.cs.yale.edu/homes/aspnes/pinewiki/QuickSelect.html. Time is O(n)'''
class Solution(object):
    def findKthLargest(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        pivot = random.choice(nums)
        left, right = [], []
        for num in nums:
            if num < pivot:
                left.append(num)
            elif num > pivot:
                right.append(num)
        if k <= len(right):
            return self.findKthLargest(right, k)
        if k > len(nums) - len(left):
            return self.findKthLargest(left, k - (len(nums) - len(left)))
            
        return pivot
