class Solution:
    def nextGreaterElement(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: List[int]
        """
        res = []
        stack = []
        m = {}
        for num in nums2:
            while len(stack) != 0 and stack[-1] < num:
                m[stack[-1]] = num
                stack.pop()
            stack.append(num)
        for num in nums1:
            if num in m:
                res.append(m[num])
            else:
                res.append(-1)
        return res
