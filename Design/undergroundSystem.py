class UndergroundSystem:

    def __init__(self):
        self.data = {}
        self.res = collections.defaultdict(dict)

    def checkIn(self, id: int, stationName: str, t: int) -> None:
        self.data[id] = [stationName, t]

    def checkOut(self, id: int, stationName: str, t: int) -> None:
        if stationName not in self.res[self.data[id][0]]:
            self.res[self.data[id][0]][stationName] = [0, 0]
        self.res[self.data[id][0]][stationName][0] += t - self.data[id][1]
        self.res[self.data[id][0]][stationName][1] += 1

    def getAverageTime(self, startStation: str, endStation: str) -> float:
        return self.res[startStation][endStation][0] / self.res[startStation][endStation][1]


# Your UndergroundSystem object will be instantiated and called as such:
# obj = UndergroundSystem()
# obj.checkIn(id,stationName,t)
# obj.checkOut(id,stationName,t)
# param_3 = obj.getAverageTime(startStation,endStation)
