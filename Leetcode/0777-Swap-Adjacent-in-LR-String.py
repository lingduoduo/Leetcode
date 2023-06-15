class Solution:
    def canTransform(self, start: str, end: str) -> bool:
        N = len(start)
        sR = eR = sL = eL = 0
        for x in range(N):
            if start[x] == "R":
                sR += 1
            if end[x] == "R":
                eR += 1
            if sR < eR:
                return False
        if sR != eR:
            return False

        for x in range(N - 1, -1, -1):
            if start[x] == "L":
                sL += 1
            if end[x] == "L":
                eL += 1
            if sL < eL:
                return False
        if sL != eL:
            return False

        start, end = start.replace("X", ""), end.replace("X", "")
        return start.split("R") == end.split("R")
