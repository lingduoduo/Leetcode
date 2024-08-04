# """
# This is GridMaster's API interface.
# You should not implement it, or speculate about its implementation
# """
#class GridMaster(object):
#    def canMove(self, direction: str) -> bool:
#
#
#    def move(self, direction: str) -> bool:
#
#
#    def isTarget(self) -> None:
#
#
from collections import deque


class Solution(object):
    def findShortestPath(self, master: 'GridMaster') -> int:
        opposite = {'U': 'D', 'D': 'U', 'L': 'R', 'R': 'L'}
        seen = set([(0, 0)])
        target = None

        def dfs(cur, x, y):  # dfs to explore the grid
            nonlocal target
            if cur.isTarget():
                target = x, y  # save `target` position
                return True
            res = False
            for di, (i, j) in zip(['D', 'U', 'L', 'R'], [(-1, 0), (1, 0), (0, -1), (0, 1)]):
                _x, _y = x + i, y + j
                if (_x, _y) not in seen and cur.canMove(di):  # if not reachable and can move
                    cur.move(di)
                    seen.add((_x, _y))  # save position to `reachable`
                    res |= dfs(cur, _x, _y)  # dfs on next position
                    cur.move(opposite[di])  # move back to position before dfs
            return res

        if not dfs(master, 0, 0): return -1

        dq = deque([(0, 0, 0)])  # starting BFS here
        while dq:
            step, x, y = dq.popleft()
            if (x, y) == target:
                return step
            for i, j in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
                _x, _y = x + i, y + j
                if (_x, _y) not in seen: continue  # only continue BFS on reachable neighbors
                dq.append((step + 1, _x, _y))  # BFS at neighbor positions
                seen.remove((_x, _y))  # remove from `reachable` once used to avoid repeats
        return -1