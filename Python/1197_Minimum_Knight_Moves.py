from collections import deque

class Solution:
    def minKnightMoves(self, x: int, y: int) -> int:
        que = deque([])
        que.append((0, 0))
        step = 0
        visited = set((0, 0))
        while que:
            for _ in range(len(que)):
                i, j = que.popleft()
                if (i, j) == (x, y):
                    return step
                for dx, dy in [(1, 2), (2, 1), (2, -1), (1, -2),(-1, -2), (-2, -1), (-2, 1), (-1, 2)]:
                    nx, ny = i + dx, j + dy
                    if (nx, ny) not in visited:
                        que.append([nx, ny])
                        visited.add((nx, ny))
            step += 1
        return step

class Solution:
    def minKnightMoves(self, x: int, y: int) -> int:
        x, y = abs(x), abs(y)
        if x < y:  # normalize to reduce states (optional but helps)
            x, y = y, x

        # small fast exits
        if x == 0 and y == 0:
            return 0
        if x == 1 and y == 0:
            return 3
        if x == 2 and y == 2:
            return 4

        moves = [(1, 2), (2, 1), (2, -1), (1, -2),
                 (-1, -2), (-2, -1), (-2, 1), (-1, 2)]

        # Bidirectional BFS: expand from start and target
        front = {(0, 0)}
        back = {(x, y)}
        visited_front = {(0, 0)}
        visited_back = {(x, y)}

        steps = 0

        # Bound the search to a tight box with buffer.
        # With abs + swap, optimal paths never need to go far outside this region.
        min_x, min_y = -2, -2
        max_x, max_y = x + 2, y + 2

        while front and back:
            # Always expand the smaller frontier
            if len(front) > len(back):
                front, back = back, front
                visited_front, visited_back = visited_back, visited_front

            next_front = set()
            for cx, cy in front:
                if (cx, cy) in visited_back:
                    return steps

                for dx, dy in moves:
                    nx, ny = cx + dx, cy + dy

                    if nx < min_x or ny < min_y or nx > max_x or ny > max_y:
                        continue

                    if (nx, ny) in visited_front:
                        continue

                    if (nx, ny) in visited_back:
                        return steps + 1

                    visited_front.add((nx, ny))
                    next_front.add((nx, ny))

            front = next_front
            steps += 1

        return -1
