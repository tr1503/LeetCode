class MagicDictionary:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.dict = []
        

    def buildDict(self, dict):
        """
        Build a dictionary through a list of words
        :type dict: List[str]
        :rtype: void
        """
        for item in dict:
           self.dict.append(item) 
        

    def search(self, word):
        """
        Returns if there is any word in the trie that equals to the given word after modifying exactly one character
        :type word: str
        :rtype: bool
        """
        for item in self.dict:
            if len(item) != len(word):
                continue
            else:
                modified = 0
                i = 0
                while i < len(item) and i < len(word):
                    if item[i] != word[i]:
                        modified += 1
                    if modified > 1:
                        break
                    i += 1

                if modified == 1:
                    return True
                
        return False


# Your MagicDictionary object will be instantiated and called as such:
# obj = MagicDictionary()
# obj.buildDict(dict)
# param_2 = obj.search(word)
