class Solution:
    def compareVersion(self, version1, version2):
        """
        :type version1: str
        :type version2: str
        :rtype: int
        """
        n = len(version1)
        m = len(version2)
        i = 0
        j = 0
        d1 = 0
        d2 = 0
        v1 = ""
        v2 = ""
        while i < n or j < m:
            while i < n and version1[i] != '.':
                v1 += version1[i]
                i += 1
            if v1 == "":
                d1 = 0
            else:
                d1 = int(v1)
            while j < m and version2[j] != '.':
                v2 += version2[j]
                j += 1
            if v2 == "":
                d2 = 0
            else:
                d2 = int(v2)
            if d1 > d2:
                return 1
            elif d1 < d2:
                return -1
            v1 = ""
            v2 = ""
            i += 1
            j += 1
        return 0
