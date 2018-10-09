class Trie(object):
    def __init__(self):
        self.children = {}
    
    def insert(self,word):
        temp = ""
        for c in word:
            temp += c
            if temp not in self.children:
                self.children[temp] = False
        self.children[word] = True
    
    def search(self, word):
        if word not in self.children:
            return False
        return self.children[word] == True
    
    def startWith(self, prefix):
        return prefix in self.children
    
class Solution(object):
    def findWords(self, board, words):
        """
        :type board: List[List[str]]
        :type words: List[str]
        :rtype: List[str]
        """
        def dfs(board, visited, s, x, y, trie):
            if x < 0 or y < 0 or x >= len(board) or y >= len(board[0]):
                return
            if visited[x][y]:
                return
            s += board[x][y]
            if trie.startWith(s) == False:
                return
            if trie.search(s):
                res.append(s)
            visited[x][y] = True
            dfs(board, visited, s, x+1, y, trie)
            dfs(board, visited, s, x-1, y, trie)
            dfs(board, visited, s, x, y+1, trie)
            dfs(board, visited, s, x, y-1, trie)
            visited[x][y] = False
        res = []
        trie = Trie()
        for word in words:
            trie.insert(word)
        n = len(board)
        m = len(board[0])
        visited = [[False for _ in range(m)] for _ in range(n)]
        for i in range(n):
            for j in range(m):
                dfs(board, visited, "", i, j, trie)
        return list(set(res))
