class Solution(object):
    def backspaceCompare(self, S, T):
        """
        :type S: str
        :type T: str
        :rtype: bool
        """
        stack1 = []
        stack2 = []
        for c in S:
            if len(stack1) != 0 and c == '#':
                stack1.pop()
            if c != '#':
                stack1.append(c)
        for c in T:
            if len(stack2) != 0 and c == '#':
                stack2.pop()
            if c != '#':
                stack2.append(c)
        return str(stack1) == str(stack2)
