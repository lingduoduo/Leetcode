class Solution:
    def shortestDistance(
        self, maze: List[List[int]], start: List[int], destination: List[int]
    ) -> int:
        distance = [[float("inf")] * len(maze[0]) for _ in range(len(maze))]
        distance[start[0]][start[1]] = 0

        dirs = [(0, 1), (0, -1), (-1, 0), (1, 0)]
        queue = deque([start])

        while queue:
            s = queue.popleft()
            for dir in dirs:
                x, y = s[0] + dir[0], s[1] + dir[1]
                count = 0
                while 0 <= x < len(maze) and 0 <= y < len(maze[0]) and maze[x][y] == 0:
                    x += dir[0]
                    y += dir[1]
                    count += 1

                if distance[s[0]][s[1]] + count < distance[x - dir[0]][y - dir[1]]:
                    distance[x - dir[0]][y - dir[1]] = distance[s[0]][s[1]] + count
                    queue.append([x - dir[0], y - dir[1]])
        return (
            distance[destination[0]][destination[1]]
            if distance[destination[0]][destination[1]] != float("inf")
            else -1
        )
