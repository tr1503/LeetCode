'''Create a hash table for the characters and set a left pointer.
If the number of keys is more than k, move the left until the key value becomes 0 and delete key.
The result should be the larger number between length get from moving left and the last result.'''
class Solution(object):
    def lengthOfLongestSubstringKDistinct(self, s, k):
        """
        :type s: str
        :type k: int
        :rtype: int
        """
        res = 0
        left = 0
        m = {}
        for i in range(len(s)):
            if s[i] not in m:
                m[s[i]] = 1
            else:
                m[s[i]] += 1
            while len(m) > k:
                m[s[left]] -= 1
                if m[s[left]] == 0:
                    del m[s[left]]
                left += 1
            res = max(res, i - left + 1)
        return res
