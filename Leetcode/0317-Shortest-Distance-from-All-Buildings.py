from typing import List


class Solution:
    def __init__(self):
        self.empty, self.building = 0, 1
        self.direction = [(0, -1), (-1, 0), (0, 1), (1, 0)]

    def shortestDistance(self, grid: List[List[int]]) -> int:
        buildings = []
        candidate_lands = {}  # {position: distance}
        building_reach = {}  # {position: number of buildings reached}

        for r in range(len(grid)):
            for c in range(len(grid[0])):
                if grid[r][c] == self.building:
                    buildings.append((r, c))
                elif grid[r][c] == self.empty:
                    candidate_lands[(r, c)] = 0
                    building_reach[(r, c)] = 0

        for building_position in buildings:
            self.compute_shortest_distances_bfs(
                candidate_lands, building_reach, building_position, grid
            )

        # Filter lands that are reachable by all buildings
        results = [
            candidate_lands[pos]
            for pos, count in building_reach.items()
            if count == len(buildings)
        ]
        return min(results) if results else -1

    def compute_shortest_distances_bfs(
        self,
        candidate_lands: dict,
        building_reach: dict,
        position: Tuple[int, int],
        grid: List[List[int]],
    ):
        rows, cols = len(grid), len(grid[0])
        distance = 0
        visited = set()
        curr_level = [position]

        while curr_level:
            distance += 1
            next_level = []

            for pos in curr_level:
                for direction in self.direction:
                    adjacent_position = (pos[0] + direction[0], pos[1] + direction[1])

                    if (
                        0 <= adjacent_position[0] < rows
                        and 0 <= adjacent_position[1] < cols
                        and grid[adjacent_position[0]][adjacent_position[1]]
                        == self.empty
                        and adjacent_position not in visited
                    ):
                        visited.add(adjacent_position)
                        next_level.append(adjacent_position)
                        candidate_lands[adjacent_position] += distance
                        building_reach[adjacent_position] += 1

            curr_level = next_level
