import heapq

class Solution:
    def swimInWater(self, grid: List[List[int]]) -> int:
        n = len(grid)
        res = float("-inf")
        nodes = []
        heapq.heappush(nodes, (grid[0][0], 0, 0))
        visited = set()

        while nodes:
            val, i, j = heapq.heappop(nodes)

            if (i, j) in visited:
                continue
            visited.add((i, j))

            res = max(res, val)
            if i == n - 1 and j == n - 1:
                return res

            for dx, dy in [[-1, 0], [1, 0], [0, -1], [0, 1]]:
                nx, ny = i + dx, j + dy
                if 0 <= nx < n and 0 <= ny < n and (nx, ny) not in visited:
                    heapq.heappush(nodes, (grid[nx][ny], nx, ny))

        return res