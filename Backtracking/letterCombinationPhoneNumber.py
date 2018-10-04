class Solution(object):
    def letterCombinations(self, digits):
        """
        :type digits: str
        :rtype: List[str]
        """
        if not digits:
            return []
        m = {"2":"abc", "3":"def", "4":"ghi", "5":"jkl", "6":"mno", "7":"pqrs", "8":"tuv", "9":"wxyz"}
        res = []
        
        def backTrack(i, cur):
            #boundary situation
            if i == len(digits):
                if len(cur) >= 0:
                    res.append(''.join(cur))
                return
            for c in m[digits[i]]:
                cur.append(c)
                backTrack(i+1,cur)
                #Backtrack, so delete last node
                cur.pop()
        backTrack(0,[])
        return res
