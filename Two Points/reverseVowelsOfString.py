class Solution:
    def reverseVowels(self, s):
        """
        :type s: str
        :rtype: str
        """
        i = 0
        j = len(s) - 1
        s = list(s)
        while i < j:
            if s[i] in 'aoeiuAOEIU' and s[j] in 'aoeiuAOEIU':
                temp = s[i]
                s[i] = s[j]
                s[j] = temp
                i += 1
                j -= 1
            elif s[i] in 'aoeiuAOEIU' and s[j] not in 'aoeiuAOEIU':
                j -= 1
            elif s[i] not in 'aoeiuAOEIU' and s[j] in 'aoeiuAOEIU':
                i += 1
            else:
                i += 1
                j -= 1
        res = ""
        for c in s:
            res += c
        return res
