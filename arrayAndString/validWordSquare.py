class Solution(object):
    def validWordSquare(self, words):
        """
        :type words: List[str]
        :rtype: bool
        """
        '''map(None, *words):
        [         [
        abc       a b c    
        ef    ->  e f None   
        ]         ]'''   
        t = map(None, *words)
        return t == map(None, *t)
