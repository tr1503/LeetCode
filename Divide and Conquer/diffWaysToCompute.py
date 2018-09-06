'''Use divide and conquer to partition the input to left and right. 
Use recursion to calculate left's and right's result. 
Finally use Cartesian product to calculate result, store to a dictionary and return result.
Dictionary can memorize the result that can be used in next time.'''
class Solution(object):   
    def calculate(self, a, b, op):
        if op == '+':
            return a + b
        elif op == '-':
            return a - b
        elif op == '*':
            return a * b
        
    def diffWaysToCompute(self, input):
        """
        :type input: str
        :rtype: List[int]
        """
        def helper(input):
            if input.isdigit():
                return [int(input)]
            if input in dict:
                return dict[input]
            result = []
            for i in range(len(input)):
                if input[i] == '+' or input[i] == '-' or input[i] == '*':
                    left = helper(input[:i])
                    right = helper(input[i+1:])
                    
                    for a in left:
                        for b in right:
                            result.append(self.calculate(a, b, input[i]))
            dict[input] = result
            return result
        
        dict = {}
        return helper(input)  
