# use an array to reprent the number of each character in string
# if one character's number is more than or missing in other string, they are not anagram
# time is O(n), space is O(1)
class Solution(object):
    def isAnagram(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        if len(s) != len(t):
            return False
        count = [0] * 26
        for c in s:
            count[ord(c) - ord('a')] += 1
        for c in t:
            count[ord(c) - ord('a')] -= 1
            if count[ord(c) - ord('a')] < 0:
                return False
        return True
