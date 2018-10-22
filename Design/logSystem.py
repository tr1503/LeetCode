class LogSystem:

    def __init__(self):
        self.unit = ["Year","Month","Day","Hour","Minute","Second"]
        self.indices = [4,7,10,13,15,19]
        self.timestamps = []

    def put(self, id, timestamp):
        """
        :type id: int
        :type timestamp: str
        :rtype: void
        """
        self.timestamps.append([id, timestamp])
        
    def retrieve(self, s, e, gra):
        """
        :type s: str
        :type e: str
        :type gra: str
        :rtype: List[int]
        """
        res = []
        index = self.unit.index(gra)
        for p in self.timestamps:
            t = p[1]
            position = self.indices[index]
            cmp1 = (t[:position] > s[:position]) - (t[:position] < s[:position])
            cmp2 = (t[:position] > e[:position]) - (t[:position] < e[:position])
            if cmp1 >= 0 and cmp2 <= 0:
                res.append(p[0])
        return res
        


# Your LogSystem object will be instantiated and called as such:
# obj = LogSystem()
# obj.put(id,timestamp)
# param_2 = obj.retrieve(s,e,gra)
