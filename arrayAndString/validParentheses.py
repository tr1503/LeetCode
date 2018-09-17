class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        check = []
        for i in range(len(s)):
            if len(check) == 0:
                check.append(s[i])
                continue
            if (s[i] == ')' and check[-1] == '(') or (s[i] == ']' and check[-1] == '[') or (s[i] == '}' and check[-1] == '{'):
                check.pop()
            else:
                check.append(s[i])
        return len(check) == 0
