'''Use divide and conquer to divide find median problem to find kth element in two sorted arrays.'''
class Solution(object):
    def findKthElement(self, nums1, s1, nums2, s2, k):
        #If start index is out of list, the kth element is in the other array.
        if s1 >= len(nums1):
            return nums2[s2 + k - 1]
        if s2 >= len(nums2):
            return nums1[s1 + k - 1]
        #If there is only one element in both arrays after recursion. Return minimum.
        if k == 1:
            return min(nums1[s1], nums2[s2])
        
        #Get first array's k/2 and second array's k/2.
        if s1 + k/2 - 1 < len(nums1):
            value1 = nums1[s1 + k/2 - 1]
        else:
            value1 = float('inf')
        if s2 + k/2 -1 < len(nums2):
            value2 = nums2[s2 + k/2 - 1]
        else:
            value2 = float('inf')
        
        #Compare them. If first array's k/2 > the another, delete the another's half. Vice Verse.
        if value1 > value2:
            return self.findKthElement(nums1, s1, nums2, s2 + k/2, k-k/2)
        else:
            return self.findKthElement(nums1, s1 + k/2, nums2, s2, k-k/2)
        
    def findMedianSortedArrays(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: float
        """
        if (len(nums1) + len(nums2)) % 2 == 1:
            return self.findKthElement(nums1, 0, nums2, 0, (len(nums1) + len(nums2)) / 2 + 1)
        else:
            return (self.findKthElement(nums1, 0, nums2, 0, (len(nums1) + len(nums2)) / 2) + self.findKthElement(nums1, 0, nums2, 0, (len(nums1) + len(nums2)) / 2 + 1)) / 2.0
