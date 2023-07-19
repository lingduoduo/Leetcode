from typing import List


class Solution:
    def wallsAndGates(self, rooms: List[List[int]]) -> None:
        """
        Do not return anything, modify rooms in-place instead.
        """

        def dfs(row, col, score):
            if rooms[row][col] == -1:
                return

            rooms[row][col] = min(rooms[row][col], score)
            dirs = [[0, 1], [0, -1], [1, 0], [-1, 0]]
            for dir in dirs:
                x, y = row + dir[0], col + dir[1]
                if 0 <= x < len(rooms) and 0 <= y < len(rooms[0]) and rooms[x][y] > 0:
                    dfs(x, y, score + 1)

        for i in range(len(rooms)):
            for j in range(len(rooms[0])):
                if rooms[i][j] == 0:
                    dfs(i, j, 0)
