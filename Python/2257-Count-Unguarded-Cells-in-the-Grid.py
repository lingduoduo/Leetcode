from typing import List

class Solution:
    UNGUARDED = 0
    GUARDED = 1
    GUARD = 2
    WALL = 3

    def _mark_direction(
        self, row: int, col: int, dr: int, dc: int, grid: List[List[int]]
    ) -> None:
        m, n = len(grid), len(grid[0])
        r, c = row + dr, col + dc

        # Move in a straight line until we hit a wall or another guard or boundary
        while 0 <= r < m and 0 <= c < n:
            if grid[r][c] == self.WALL or grid[r][c] == self.GUARD:
                break
            if grid[r][c] == self.UNGUARDED:
                grid[r][c] = self.GUARDED
            r += dr
            c += dc

    def countUnguarded(
        self, m: int, n: int, guards: List[List[int]], walls: List[List[int]]
    ) -> int:
        grid = [[self.UNGUARDED] * n for _ in range(m)]

        # Mark guards' positions
        for r, c in guards:
            grid[r][c] = self.GUARD

        # Mark walls' positions
        for r, c in walls:
            grid[r][c] = self.WALL

        # Mark cells as guarded by traversing from each guard
        for gr, gc in guards:
            for dr, dc in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
                self._mark_direction(gr, gc, dr, dc, grid)

        # Count unguarded cells
        return sum(row.count(self.UNGUARDED) for row in grid)
