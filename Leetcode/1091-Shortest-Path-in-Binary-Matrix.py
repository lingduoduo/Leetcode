class Solution:
    def shortestPathBinaryMatrix(self, grid: List[List[int]]) -> int:
        m = len(grid)
        n = len(grid[0])
        
        if grid[0][0] == 1 or grid[-1][-1] == 1:
            return -1

        if m == 1 and grid[0][0] == 0:
            return 1

        stack = []
        stack.append((0, 0))
        
        visited = [[0]*n for _ in range(m)]
        visited[0][0] = 1

        directions = [ [-1, -1], [-1, 0], [-1, 1], [0, -1], [0, 1], [1, -1], [1, 0], [1, 1]]

        step = 1
        while stack:
            size = len(stack)
            for i in range(size):
                x, y = stack.pop(0)
                for d in directions:
                    dx, dy = x + d[0], y + d[1]
                    if dx <0 or dx >= m or dy < 0 or dy >= n or grid[dx][dy] == 1 or visited[dx][dy] == 1:
                        continue
                    if dx == n-1 and dy == m-1:
                        return step + 1
                    visited[dx][dy] = 1
                    stack.append((dx, dy))
            step += 1
        return -1


class Solution:
    def shortestPathBinaryMatrix(self, grid: List[List[int]]) -> int:
        max_row = len(grid) - 1
        max_col = len(grid[0]) - 1
        directions = [(-1, -1), (-1, 0), (-1, 1), (0, -1), (0, 1), (1, -1), (1, 0), (1, 1)]

        # Helper function to find the neighbors of a given cell.
        def get_neighbours(row, col):
            for row_difference, col_difference in directions:
                new_row = row + row_difference
                new_col = col + col_difference
                if not (0 <= new_row <= max_row and 0 <= new_col <= max_col):
                    continue
                if grid[new_row][new_col] != 0:
                    continue
                yield (new_row, new_col)

        # Check that the first and last cells are open.
        if grid[0][0] != 0 or grid[max_row][max_col] != 0:
            return -1

        # Set up the BFS.
        queue = deque()
        queue.append((0, 0))
        grid[0][0] = 1

        # Carry out the BFS.
        while queue:
            row, col = queue.popleft()
            distance = grid[row][col]
            if (row, col) == (max_row, max_col):
                return distance
            for neighbour_row, neighbour_col in get_neighbours(row, col):
                grid[neighbour_row][neighbour_col] = distance + 1
                queue.append((neighbour_row, neighbour_col))

        # There was no path.
        return -1
    