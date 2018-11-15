# Use sort instead of heap + hash map to solve this question
# Create an array which represents the count of each character firstly, each time + 100, sort it.
# Then use count % 100 + ord('a') to get the character's ACSII and convert to original character
# Finally to put each character based on appearing time from small to large. 
# Use index += 2 to prevent the same character together. If iter beyond the array, back to start
class Solution:
    def reorganizeString(self, S):
        """
        :type S: str
        :rtype: str
        """
        n = len(S)
        index = 1
        count = [0] * 26
        for c in S:
            count[ord(c) - ord('a')] += 100
        for i in range(26):
            count[i] += i
        count.sort()
        res = list(S)
        for num in count:
            t = num // 100
            ch = chr((num % 100) + ord('a'))
            if t > (n + 1) // 2:
                return ""
            for i in range(t):
                if index >= n:
                    index = 0
                res[index] = ch
                index += 2
        return "".join(res)
