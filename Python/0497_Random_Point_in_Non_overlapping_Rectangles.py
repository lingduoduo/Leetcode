class Solution:
    def __init__(self, rects: List[List[int]]):
        self.rects = rects
        rect = rects[0]

        self.areas = [(rect[2] - rect[0] + 1) * (rect[3] - rect[1] + 1)]
        for rect in rects[1:]:
            curarea = (rect[2] - rect[0] + 1) * (rect[3] - rect[1] + 1)
            self.areas.append(self.areas[-1] + curarea)
        self.tot = self.areas[-1]

    def pick(self) -> List[int]:
        ran = random.randint(1, self.tot)
        ind = bisect.bisect_left(self.areas, ran)
        rect = self.rects[ind]
        return [random.randint(rect[0], rect[2]), random.randint(rect[1], rect[3])]


# Your Solution object will be instantiated and called as such:
# obj = Solution(rects)
# param_1 = obj.pick()
