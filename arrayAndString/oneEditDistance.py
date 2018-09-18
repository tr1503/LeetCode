class Solution(object):
    def isOneEditDistance(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        if not s and not t:
            return False
        if len(s) < len(t):
            temp = s
            s = t
            t = temp
        #If diff of s and t > 1, it needs two step, so return False.
        if len(s) - len(t) > 1:
            return False
        #If diff of s and t = 1, only needs to check the string after the first different character.
        if len(s) - len(t) == 1:
            for i in range(len(t)):
                if s[i] != t[i]:
                    return s[i+1:] == t[i:]
            return True
        #If diff of s and t = 0, only needs to check the different characters = 1. 
        #If it is 0, return False because no any change.
        else:
            count = 0
            for i in range (len(s)):
                if s[i] != t[i]:
                    count += 1
                    if count > 1:
                        return False
            if count == 0:
                return False
            return True
