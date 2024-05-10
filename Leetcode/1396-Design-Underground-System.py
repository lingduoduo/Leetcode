from  collections import defaultdict


class UndergroundSystem:
    def __init__(self):
        self.user = {}
        self.station = defaultdict(lambda: defaultdict(list))

    def checkIn(self, id: int, stationName: str, t: int) -> None:
        self.user[id] = (stationName, t)

    def checkOut(self, id: int, stationName: str, t: int) -> None:
        stationStart, t0 = self.user[id]
        self.station[(stationStart, stationName)].append(t - t0)

    def getAverageTime(self, startStation: str, endStation: str) -> float:
        l = self.station[(startStation, endStation)]
        return sum(l) / len(l)


# Your UndergroundSystem object will be instantiated and called as such:
# obj = UndergroundSystem()
# obj.checkIn(id,stationName,t)
# obj.checkOut(id,stationName,t)
# param_3 = obj.getAverageTime(startStation,endStation)
