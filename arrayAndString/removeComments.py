class Solution:
    def removeComments(self, source):
        """
        :type source: List[str]
        :rtype: List[str]
        """
        res = []
        comment = False
        out = ""
        for line in source:
            i = 0
            while i < len(line):
                if not comment:
                    if i == len(line) - 1:
                        out += line[i]
                    else:
                        temp = line[i:i+2]
                        if temp == "/*":
                            comment = True
                            i += 1
                        elif temp == "//":
                            break
                        else:
                            out += line[i]
                else:
                    if i < len(line) - 1:
                        temp = line[i:i+2]
                        if temp == "*/":
                            comment = False
                            i += 1
                i += 1
            if out != "" and not comment:
                res.append(out)
                out = ""
        return res
