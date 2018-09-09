class Solution(object):
    def merge(self, nums1, m, nums2, n):
        """
        :type nums1: List[int]
        :type m: int
        :type nums2: List[int]
        :type n: int
        :rtype: void Do not return anything, modify nums1 in-place instead.
        """
        i = m - 1 #The last valid value in array one
        j = n - 1 
        key = m + n - 1 #The last value in array one
        #Merge from the last to start. 
        while i >= 0 and j >= 0:
            if nums1[i] > nums2[j]:
                nums1[key] = nums1[i]
                i -= 1
            else:
                nums1[key] = nums2[j]
                j -= 1
            key -= 1
        #If array one still has numbers but array two doesn't, array one is a sorted list now.
        #If array two still has numbers, put them to rest of spot in array one.
        while j >= 0:
            nums1[key] = nums2[j]
            j -= 1
            key -= 1
