'''Get the times need to repeat A. It should be +3 because the features of Python.
During the loop, once B is substring of A, return current loop times.
If after the loop, B is not substring of A. Then return -1.'''
class Solution(object):
    def repeatedStringMatch(self, A, B):
        """
        :type A: str
        :type B: str
        :rtype: int
        """
        times = len(B) / len(A) + 3
        for i in range(1,times):
            if B in A * i:
                return i
        return -1
