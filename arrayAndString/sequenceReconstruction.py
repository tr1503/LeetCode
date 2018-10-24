class Solution:
    def sequenceReconstruction(self, org, seqs):
        """
        :type org: List[int]
        :type seqs: List[List[int]]
        :rtype: bool
        """
        if not seqs:
            return False
        n = len(org)
        count = n - 1
        pos = [0] * (n + 1)
        flags = [0] * (n + 1)
        existed = False
        for i in range(n):
            pos[org[i]] = i
        for seq in seqs:
            for i in range(len(seq)):
                existed = True
                if seq[i] <= 0 or seq[i] > n:
                    return False
                if i == 0:
                    continue
                pre = seq[i-1]
                curr = seq[i]
                if pos[pre] >= pos[curr]:
                    return False
                if flags[curr] == 0 and pos[pre] + 1 == pos[curr]:
                    flags[curr] = 1
                    count -= 1
        return count == 0 and existed
        
