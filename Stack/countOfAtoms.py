class Solution:
    def countOfAtoms(self, formula: str) -> str:
        counter = collections.Counter()
        n = len(formula)
        
        count = 1
        stack = []
        weight = 1
        i = n - 1
        
        while i >= 0:
            low = ""
            count = 1
            if formula[i].isdigit():
                j = i
                while i >= 0 and formula[i].isdigit():
                    i -= 1
                count = int(formula[i+1:j+1])
            
            if formula[i] == ')':
                weight *= count
                stack.append(count)
            elif formula[i] == '(':
                weight //= stack.pop()
            elif formula[i].islower():
                low = formula[i]
                i -= 1
            if formula[i].isupper():
                e = formula[i] + low
                counter[e] += count * weight
            i -= 1
        
        res = ""
        for e in sorted(counter.keys()):
            res += e
            if counter[e] > 1:
                res += str(counter[e])
        return res
