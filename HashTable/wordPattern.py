#Use two hashmap to hash pattern to str and str to pattern
class Solution:
    def wordPattern(self, pattern, str):
        """
        :type pattern: str
        :type str: str
        :rtype: bool
        """
        m = {}
        n = {}
        words = str.split(' ')
        if len(pattern) != len(words):
            return False
        for p, s in zip(pattern, words):
            if p not in m and s not in n:
                m[p] = s
                n[s] = p
            else:
                if s not in n or p not in m or n[s] != p or m[p] != s:
                    return False
        return True
