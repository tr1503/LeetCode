class Solution(object):
    def calculate(self, s):
        """
        :type s: str
        :rtype: int
        """
        stack = []
        res = 0
        num = 0
        sign = 1
        for i in range(len(s)):
            #If it is digit, add to temp variable num
            if s[i].isdigit():
                num = 10 * num + int(s[i])
            elif s[i] == ' ':
                continue
            #+ and - need to add temp variable to result
            elif s[i] == '+':
                res += sign * num
                num = 0
                sign = 1
            elif s[i] == '-':
                res += sign * num
                num = 0
                sign = -1
            #Parentheses needs to append the result and sign to stack firstly to wait for calculating
            #Meet the close parenthsis, pop the sign firstly and dicide positive/negative
            #And then pop the stack for adding result
            elif s[i] == '(':
                stack.append(res)
                stack.append(sign)
                res = 0
                sign = 1
            elif s[i] == ')':
                res += sign * num
                num = 0
                res *= stack[-1]
                stack.pop()
                res += stack[-1]
                stack.pop()
                
        res += sign * num
        return res
