class Solution:
    def partitionLabels(self, S):
        """
        :type S: str
        :rtype: List[int]
        """
        res = []
        n = len(S)
        start = 0
        last = 0
        m = {}
        # Set every character's last appearing index in hash map
        for i in range(n):
            m[S[i]] = i
        for i in range(n):
            last = max(last, m[S[i]])
            # When the index is this character's last appearing position, set here as break point
            # Add the length to the result and set the start to i + 1
            if last == i:
                res.append(i - start + 1)
                start = i + 1
        return res
