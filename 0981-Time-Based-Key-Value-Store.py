class TimeMap:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.kv = defaultdict(list)
        

    def set(self, key: str, value: str, timestamp: int) -> None:
        self.kv[key].append([timestamp, value])

    def get(self, key: str, timestamp: int) -> str:
        d = self.kv[key]
        low = 0
        high = len(d)
        while low < high:
            mid = int((low+high) / 2)
            if d[mid][0] <= timestamp:
                low = mid + 1
            else:
                high = mid
        if high - 1 < 0:
            return ""
        else:
            return d[high-1][1]
        