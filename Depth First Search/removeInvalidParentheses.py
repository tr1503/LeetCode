class Solution:
    def removeInvalidParentheses(self, s):
        """
        :type s: str
        :rtype: List[str]
        """
        left = 0
        right = 0
        #Check the invalid parentheses:
        for c in s:
            if c == '(':
                left += 1
            elif c == ')':
                if left == 0:
                    right += 1
                if left > 0:
                    left -= 1
                    
        res = set()
        def dfs(index, left_count, right_count, left_rem, right_rem, expr):
            if index == len(s):
                if left_rem == 0 and right_rem == 0:
                    res.add(expr)
            else:
                if (s[index] == '(' and left_rem > 0) or (s[index] == ')' and right_rem > 0):
                    dfs(index + 1, left_count, right_count, left_rem - (s[index] == '('), right_rem - (s[index] == ')'), expr)
                if s[index] != '(' and s[index] != ')':
                    dfs(index + 1, left_count, right_count, left_rem, right_rem, expr + s[index])
                elif s[index] == '(':
                    dfs(index + 1, left_count+1, right_count, left_rem, right_rem, expr + '(')
                elif s[index] == ')' and left_count > right_count:
                    dfs(index + 1, left_count, right_count + 1, left_rem, right_rem, expr + ')')
                
        dfs(0,0,0,left,right,"")
        return list(res)
