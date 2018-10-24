# Sort the array firstly and iter the array to find the first element that
# is smaller the count
class Solution:
    def hIndex(self, citations):
        """
        :type citations: List[int]
        :rtype: int
        """
        n = len(citations)
        citations.sort()
        for i in range(n-1,-1,-1):
            j = n - i - 1
            if j >= citations[i]:
                return j
        return n
