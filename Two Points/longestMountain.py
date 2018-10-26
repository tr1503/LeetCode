class Solution:
    def longestMountain(self, A):
        """
        :type A: List[int]
        :rtype: int
        """
        i = 0
        n = len(A)
        res = 0
        while i < n - 1:
            # find the ascending point
            if A[i] < A[i+1]:
                j = i + 1
                while j < n and A[j] > A[j-1]:
                    j += 1
                # if iter to the end of array, return the result
                if j == n:
                    return res
                # prevent the wrong example like: [1,2,2,0]
                if A[j] != A[j-1]:
                    while j < n and A[j] < A[j-1]:
                        j += 1
                    res = max(res, j - i)
                    i = j - 2
                else:
                    i = j - 1
            i += 1
        return res
