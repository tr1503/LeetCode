# Use the stack to solve this question. Use a while loop to pop up and be replaced by
# current digit. Also, the loop needs to check the last digit in the stack is larger
# than the current digit, so it can keep the smaller digit in the stack.
class Solution:
    def removeKdigits(self, num, k):
        """
        :type num: str
        :type k: int
        :rtype: str
        """
        if len(num) == k:
            return '0'
        stack = []
        for n in num:
            while stack and k and int(stack[-1]) > int(n):
                stack.pop()
                k -= 1
            stack.append(n)
        while k:
            stack.pop()
            k -= 1
        if not stack:
            return '0'
        return str(int("".join(stack)))
