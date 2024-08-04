class Solution:
    def minAreaRect(self, points: List[List[int]]) -> int:
        n = len(points)
        nx = len(set(x for x, y in points))
        ny = len(set(y for x, y in points))
        if nx == n or ny == n:
            return 0

        p = collections.defaultdict(list)
        if nx > ny:
            for x, y in points:
                p[x].append(y)
        else:
            for x, y in points:
                p[y].append(x)

        lastx = {}
        res = float("inf")
        for x in sorted(p):
            p[x].sort()
            for i in range(len(p[x])):
                for j in range(i):
                    y1, y2 = p[x][j], p[x][i]
                    if (y1, y2) in lastx:
                        res = min(res, (x - lastx[y1, y2]) * abs(y2 - y1))
                    lastx[y1, y2] = x
        return res if res < float("inf") else 0


class Solution:
    def minAreaRect(self, points: List[List[int]]) -> int:
        columns = collections.defaultdict(list)
        for x, y in points:
            columns[x].append(y)
        lastx = {}
        ans = float("inf")

        for x in sorted(columns):
            column = columns[x]
            column.sort()
            for j, y2 in enumerate(column):
                for i in range(j):
                    y1 = column[i]
                    if (y1, y2) in lastx:
                        ans = min(ans, (x - lastx[y1, y2]) * (y2 - y1))
                    lastx[y1, y2] = x
        return ans if ans < float("inf") else 0


class Solution:
    def minAreaRect(self, points: List[List[int]]) -> int:

        horizontal = {}
        vertical = {}
        res = float('inf')

        for x, y in points:
            if y not in horizontal:
                horizontal[y] = []
            horizontal[y].append(x)
            if x not in vertical:
                vertical[x] = []
            vertical[x].append(y)


        for line in horizontal.values():
            line.sort()
        for line in vertical.values():
            line.sort()

        for x, y in points:
            for prev_x in horizontal[y]:
                if prev_x >= x:
                    continue
                for prev_y in vertical[x]:
                    if prev_y >= y:
                        continue
                    if prev_y in vertical[prev_x]:
                        res = min(res, abs(x - prev_x) * abs(y - prev_y))
        return 0 if res == float('inf') else res

        