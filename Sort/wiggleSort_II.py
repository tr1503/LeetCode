class Solution:
    def findKthLargest(self, nums, k):
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
    
    def newIndex(self, index, n):
        return (1 + 2 * index) % (n | 1)
    
    def wiggleSort(self, nums):
        """
        :type nums: List[int]
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        n = len(nums)
        if n < 2:
            return
        median = self.findKthLargest(nums, (len(nums) + 1) // 2)
        left = 0
        right = n - 1
        i = 0
        while i <= right:
            if nums[self.newIndex(i,n)] > median:
                index1 = self.newIndex(left,n)
                index2 = self.newIndex(i,n)
                nums[index1], nums[index2] = nums[index2], nums[index1]
                left += 1
                i += 1
            elif nums[self.newIndex(i,n)] < median:
                index1 = self.newIndex(right,n)
                index2 = self.newIndex(i,n)
                nums[index1], nums[index2] = nums[index2], nums[index1]
                right -= 1
            else:
                i += 1
