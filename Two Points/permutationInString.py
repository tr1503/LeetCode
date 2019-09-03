# Use two points and sliding window to solve this problem
# time is O(n + m), space is O(1)
class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        n = len(s1)
        m = len(s2)
        c1 = [0 for _ in range(26)]
        c2 = [0 for _ in range(26)]
        for c in s1:
            c1[ord(c) - ord('a')] += 1
        for i in range(m):
            if i >= n:
                c2[ord(s2[i - n]) - ord('a')] -= 1
            c2[ord(s2[i]) - ord('a')] += 1
            if c1 == c2:
                return True
        return False
