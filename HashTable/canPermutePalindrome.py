class Solution:
    def canPermutePalindrome(self, s: str) -> bool:
        m = [0 for _ in range(128)]
        count = 0
        for i in range(len(s)):
            m[ord(s[i]) - ord('a')] += 1
            if m[ord(s[i]) - ord('a')] % 2 == 0:
                count -= 1
            else:
                count += 1
        return count <= 1
