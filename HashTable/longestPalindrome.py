class Solution:
    def longestPalindrome(self, s: str) -> int:
        m = set()
        for c in s:
            if c not in m:
                m.add(c)
            else:
                m.remove(c)
        return len(s) - len(m) + 1 if len(m) > 0 else len(s)
