class Solution:
    def partition(self, s):
        """
        :type s: str
        :rtype: List[List[str]]
        """
        self.res = []
        self.dfs(s,[])
        return self.res
    
    def dfs(self,s,temp):
        if not s:
            #Copy array to other array use list[:]
            self.res.append(temp[:])
            return 
        #Backtracking
        #We need len(s) + 1 to let s to null
        for i in range(1,len(s)+1):
            if self.isPal(s[:i]):
                temp.append(s[:i])
                self.dfs(s[i:],temp) 
                temp.pop()
    
    def isPal(self,s):
        return s == s[::-1]
