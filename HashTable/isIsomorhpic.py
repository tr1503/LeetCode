class Solution:
    def isIsomorphic(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        m = {}
        n = {}
        for c in s:
            m[c] = 0
        for c in t:
            n[c] = 0
        for i in range(len(s)):
            if m[s[i]] != n[t[i]]:
                return False
            m[s[i]] = i + 1
            n[t[i]] = i + 1
        return True
