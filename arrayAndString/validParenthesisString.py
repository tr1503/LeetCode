class Solution:
    def checkValidString(self, s):
        """
        :type s: str
        :rtype: bool
        """
        if not s:
            return True
        max_op = 0
        min_op = 0
        for c in s:
            if c == '(':
                min_op += 1
            else:
                min_op -= 1
            if c != ')':
                max_op += 1
            else:
                max_op -= 1
            if max_op < 0:
                return False
            if min_op < 0:
                min_op = 0
            
        return min_op == 0
