class Solution:
    def maximumMinutes(self, grid: List[List[int]]) -> int:
        m, n = len(grid), len(grid[0])
        DIRS = [(1,0), (-1,0), (0,1), (0,-1)]
        INF = 10**15

        # 1) fire_time: earliest time fire reaches each cell
        fire_time = [[INF] * n for _ in range(m)]
        q = deque()

        for r in range(m):
            for c in range(n):
                if grid[r][c] == 1:
                    fire_time[r][c] = 0
                    q.append((r, c))
                elif grid[r][c] == 2:
                    fire_time[r][c] = -1  # wall

        while q:
            r, c = q.popleft()
            t = fire_time[r][c]
            for dr, dc in DIRS:
                nr, nc = r + dr, c + dc
                if 0 <= nr < m and 0 <= nc < n and fire_time[nr][nc] != -1:
                    if fire_time[nr][nc] > t + 1:
                        fire_time[nr][nc] = t + 1
                        q.append((nr, nc))

        # 2) can(wait): can we wait 'wait' minutes at (0,0) and still reach safehouse?
        def can(wait: int) -> bool:
            # start cell blocked
            if grid[0][0] == 2:
                return False

            # if fire reaches start at or before we start moving, we die
            ft0 = fire_time[0][0]
            if ft0 != -1 and wait >= ft0:
                return False

            dist = [[INF] * n for _ in range(m)]
            dist[0][0] = wait
            q = deque([(0, 0)])

            while q:
                r, c = q.popleft()
                t = dist[r][c]

                for dr, dc in DIRS:
                    nr, nc = r + dr, c + dc
                    if not (0 <= nr < m and 0 <= nc < n):
                        continue
                    if grid[nr][nc] == 2:
                        continue

                    nt = t + 1  # we arrive at next cell at time nt
                    ft = fire_time[nr][nc]

                    # fire constraint:
                    # - normal cells: must arrive strictly before fire (nt < ft)
                    # - safehouse: can arrive at same time (nt <= ft)
                    if ft != -1:
                        if (nr, nc) == (m - 1, n - 1):
                            if nt > ft:
                                continue
                        else:
                            if nt >= ft:
                                continue

                    if nt < dist[nr][nc]:
                        dist[nr][nc] = nt
                        q.append((nr, nc))

            return dist[m - 1][n - 1] < INF

        # 3) If we can wait forever, return 1e9
        if can(10**9):
            return 10**9

        # 4) Binary search max wait
        lo, hi = 0, 10**9
        while lo < hi:
            mid = (lo + hi + 1) // 2
            if can(mid):
                lo = mid
            else:
                hi = mid - 1

        return lo if can(lo) else -1        