class Trie(object):
    def __init__(self):
        self.children = {}
    
    def insert(self, word):
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
    
    def startWiths(self, prefix):
        return prefix in self.children
    
class Solution(object):
    def longestWord(self, words):
        """
        :type words: List[str]
        :rtype: str
        """
        trie = Trie()
        for word in words:
            trie.insert(word)
        ans = ""
        for word in words:
            temp = ""
            for c in word:
                temp += c
                if trie.search(temp) == False:
                    break
            if temp == word:
                if len(word) > len(ans) or (len(word) == len(ans) and ans > word):
                    ans = word
        return ans
