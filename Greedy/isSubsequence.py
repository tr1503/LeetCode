#Use greedy get the current character's index in t, and shorten the search range
#Check https://www.jianshu.com/p/bb4cb2684dea
class Solution(object):
    def isSubsequence(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        if not s and not t:
            return True
        if len(t) < len(s):
            return False
        if not s:
            return True
        j = 0
        target = s[0]
        for i in range(len(t)):
            curr = t[i]
            if curr == target:
                j += 1
                if j >= len(s):
                    return True
                target = s[j]
        return False
