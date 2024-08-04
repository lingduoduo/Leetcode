from typing import List
class Solution:
    def maximumInvitations(self, grid: List[List[int]]) -> int:
        m, n = len(grid), len(grid[0])
        res = {}  # Stores matches formed. key = girl, value = boy.
        def dfs(boy: int, visited: set) -> bool:
            for girl in range(n):
                if grid[boy][girl] and girl not in visited:
                    visited.add(girl)
                    if girl not in res or dfs(res[girl], visited):
                        res[girl] = boy
                        return True

            return False

        for boy in range(m):
            dfs(boy, set())

        return len(res)

if __name__ == "__main__":
    res = Solution().maximumInvitations(grid = [[1,1,1],
               [1,0,1],
               [0,0,1]])
    print(res)