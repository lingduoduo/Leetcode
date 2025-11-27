from typing import List
import collections

class Solution:
    def wallsAndGates(self, rooms: List[List[int]]) -> None:
        """
        Do not return anything, modify rooms in-place instead.
        """
        if not rooms:
            return

        r_size = len(rooms)
        c_size = len(rooms[0])
        q = collections.deque()
        for r in range(r_size):
            for c in range(c_size):
                if rooms[r][c] == 0:
                    q.append((r, c))
        dirs = [(-1, 0), (0, -1), (1, 0), (0, 1)]
        while q:
            x, y = q.popleft()
            distance = rooms[x][y] + 1
            for dx, dy in dirs:
                new_x, new_y = x + dx, y + dy
                if (
                    0 <= new_x < r_size
                    and 0 <= new_y < c_size
                    and rooms[new_x][new_y] == 2147483647
                ):
                    rooms[new_x][new_y] = distance
                    q.append((new_x, new_y))


if __name__ == "__main__":
    res = Solution().wallsAndGates(
        [
            [2147483647, -1, 0, 2147483647],
            [2147483647, 2147483647, 2147483647, -1],
            [2147483647, -1, 2147483647, -1],
            [0, -1, 2147483647, 2147483647],
        ]
    )
