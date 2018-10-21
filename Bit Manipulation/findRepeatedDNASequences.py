class Solution:
    def findRepeatedDnaSequences(self, s):
        """
        :type s: str
        :rtype: List[str]
        """
        res = set()
        m = set()
        i = 0
        while i + 9 < len(s):
            t = s[i:i+10]
            if t in m:
                res.add(t)
            else:
                m.add(t)
            i += 1
        return list(res)
