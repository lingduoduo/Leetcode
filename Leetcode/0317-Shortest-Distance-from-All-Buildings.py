
from typing import List, Tuple, Dict

class Solution:

    def shortest_distance(self, grid: List[List[int]]) -> int:
        bldgs = []
        lands = {}  # {position: distance}
        reach = {}  # {position: number of buildings reached}

        for r in range(len(grid)):
            for c in range(len(grid[0])):
                if grid[r][c] == 1:
                    bldgs.append((r, c))
                elif grid[r][c] == 0:
                    lands[(r, c)] = 0
                    reach[(r, c)] = 0

        for bldg in bldgs:
            self.bfs(lands, reach, bldg, grid)

        results = [dist for pos, dist in lands.items() if reach[pos] == len(bldgs)]
        return min(results, default=-1)

    def bfs(self, lands: Dict[Tuple[int, int], int], reach: Dict[Tuple[int, int], int], start: Tuple[int, int], grid: List[List[int]]):
        rows, cols = len(grid), len(grid[0])
        dist = 0
        visited = set([start])
        curr_level = [start]

        while curr_level:
            dist += 1
            next_level = []

            for r, c in curr_level:
                for dr, dc in  [(0, -1), (-1, 0), (0, 1), (1, 0)]:
                    nr, nc = r + dr, c + dc

                    if 0 <= nr < rows and 0 <= nc < cols and grid[nr][nc] == 0 and (nr, nc) not in visited:
                        visited.add((nr, nc))
                        next_level.append((nr, nc))
                        lands[(nr, nc)] += dist
                        reach[(nr, nc)] += 1

            curr_level = next_level
