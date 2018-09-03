class Trie(object):

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.children = {}

    def insert(self, word):
        """
        Inserts a word into the trie.
        :type word: str
        :rtype: void
        """
        temp = ""
        for c in word:
            temp += c
            if temp not in self.children:
                self.children[temp] = False
        self.children[word] = True

    def search(self, word):
        """
        Returns if the word is in the trie.
        :type word: str
        :rtype: bool
        """
        if word not in self.children:
            return False
        return self.children[word] == True
        

    def startsWith(self, prefix):
        """
        Returns if there is any word in the trie that starts with the given prefix.
        :type prefix: str
        :rtype: bool
        """
        return prefix in self.children


# Your Trie object will be instantiated and called as such:
# obj = Trie()
# obj.insert(word)
# param_2 = obj.search(word)
# param_3 = obj.startsWith(prefix)