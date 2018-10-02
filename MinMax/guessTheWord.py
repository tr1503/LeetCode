# """
# This is Master's API interface.
# You should not implement it, or speculate about its implementation
# """
#class Master(object):
#    def guess(self, word):
#        """
#        :type word: str
#        :rtype int
#        """

class Solution(object):
    def match(self, a, b):
        count = 0
        for i in range(len(a)):
            if a[i] == b[i]:
                count += 1
        return count
    
    def find(self, w, master):
        if not w:
            return
        x = random.randint(0,len(w)-1)
        guess = master.guess(w[x])
        #Create a new list for same match number's word
        temp = []
        for i in range(len(w)):
            if i != x and self.match(w[i],w[x]) == guess:
                temp.append(w[i])
        self.find(temp,master)
            
    def findSecretWord(self, wordlist, master):
        """
        :type wordlist: List[Str]
        :type master: Master
        :rtype: None
        """
        self.find(wordlist,master)
