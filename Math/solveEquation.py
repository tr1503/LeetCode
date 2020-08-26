class Solution:
    def solveEquation(self, equation: str) -> str:
        def helper(s):
            coef = 0
            constant = 0
            s += ' '
            i = 0
            for j, c in enumerate(s):
                if j != i and c in '+- ':
                    expr = s[i:j]
                    i = j
                    if expr[-1] == 'x':
                        expr = expr[:-1]
                        if expr in '+-':
                            expr += '1'
                        coef += int(expr)
                    else:
                        constant += int(expr)
            return coef, constant
        
        left, right = equation.split('=')
        k1, b1 = helper(left)
        k2, b2 = helper(right)
        if k1 != k2 and b1 != b2:
            res = 'x=' + str((b2 - b1) // (k1 - k2))
        else:
            if k1 == k2 and b1 == b2:
                res = "Infinite solutions"
            else:
                if b2 != b1:
                    res = "No solution"
                else:
                    res = "x=0"
        return res
