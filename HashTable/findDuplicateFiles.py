# Use each file's content as the key and path as the value. 
class Solution:
    def buildHashMap(self, paths, m):
        for path in paths:
            lst = path.split()
            folder = lst[0]
            for i in range(1, len(lst)):
                fileName, fileContent = lst[i].split('(')
                fileContent = fileContent[:-1]
                group = m.setdefault(fileContent, [])
                group.append(folder + '/' + fileName)
        
    def findDuplicate(self, paths):
        """
        :type paths: List[str]
        :rtype: List[List[str]]
        """
        res = []
        m = {}
        self.buildHashMap(paths, m)
        return [v for v in m.values() if len(v) > 1]
