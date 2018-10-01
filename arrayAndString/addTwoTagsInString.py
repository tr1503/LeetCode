class Solution(object):
    def addBoldTag(self, s, dict):
        """
        :type s: str
        :type dict: List[str]
        :rtype: str
        """
        res = ""
        i = 0
        r = -1
        while i < len(s):
            found = False
            for word in dict:
                if s[i:].startswith(word):
                    if found is False and r < i:
                        res += "<b>"
                    found = True
                    r = max(r, i + len(word))
            if r == i:
                res += "</b>"
            res += s[i]
            i += 1
        
        if r == len(s):
            res += "</b>"
        return res
