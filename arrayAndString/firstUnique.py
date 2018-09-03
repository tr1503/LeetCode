class Solution(object):
    def firstUniqChar(self, s):
        """
        :type s: str
        :rtype: int
        """
        count = {}
        for c in s:
            if c not in count:
                count[c] = 1
            else:
                count[c] += 1
        for i in range(0, len(s), 1):
            if count[s[i]] == 1:
                return i
        return -1   
