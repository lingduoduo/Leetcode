class Solution:
    def minimumEffortPath(self, heights: List[List[int]]) -> int:
        m, n = len(heights), len(heights[0])
        distances = defaultdict(lambda: float("inf"))
        dirs = [(0, -1), (0, 1), (-1, 0), (1, 0)]
        q = []
        heappush(q, (0, 0, 0))
        while q:
            effort, curx, cury = heappop(q)
            if (curx, cury) == (m - 1, n - 1):
                return effort
            for dx, dy in dirs:
                tx, ty = curx + dx, cury + dy
                if 0 <= tx < m and 0 <= ty < n:
                    tmp = max(effort, abs(heights[tx][ty] - heights[curx][cury]))
                    if distances[(tx, ty)] > tmp:
                        distances[(tx, ty)] = tmp
                        heappush(q, (tmp, tx, ty))
