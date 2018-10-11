class Solution(object):
    def calculate(self, a, b, op):
        if op == '+':
            return a + b
        elif op == '-':
            return a - b
        elif op == '*':
            return a * b
        elif op == '/':
            return a / b 
        
    def evalRPN(self, tokens):
        """
        :type tokens: List[str]
        :rtype: int
        """
        stack = []
        for c in tokens:
            if c.lstrip('-').isdigit():
                stack.append(c)
            else:
                num2 = stack.pop()
                num1 = stack.pop()
                stack.append(self.calculate(int(num1),int(num2),c))   
        return int(stack[0])
