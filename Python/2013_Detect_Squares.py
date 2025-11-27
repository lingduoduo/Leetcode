class DetectSquares:

    def __init__(self):
        self.d = collections.defaultdict(int)

    def add(self, point: List[int]) -> None:
        self.d[tuple(point)] += 1
        

    def count(self, point: List[int]) -> int:
        res = 0
        x1, y1 = point

        for (x2, y2), n in self.d.items():
            x_dist, y_dist = abs(x1 - x2), abs(y1 - y2)
            if x_dist == y_dist and x_dist > 0:
                corner1 = (x1, y2)
                corner2 = (x2, y1)
                if corner1 in self.d and corner2 in self.d:
                    res += n * self.d[corner1] * self.d[corner2]

        return res
        


# Your DetectSquares object will be instantiated and called as such:
# obj = DetectSquares()
# obj.add(point)
# param_2 = obj.count(point)