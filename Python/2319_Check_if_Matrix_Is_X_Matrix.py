from typing import List


class Solution:
    def checkXMatrix(self, grid: List[List[int]]) -> bool:
        diag = []
        nondiag = []
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if i == j or i + j == len(grid) - 1:
                    diag.append(grid[i][j])
                else:
                    nondiag.append(grid[i][j])
        print(diag)
        print(nondiag)
        return all([v != 0 for v in diag]) and all([v == 0 for v in nondiag])


if __name__ == "__main__":
    res = Solution().checkXMatrix(
        grid=[[2, 0, 0, 1], [0, 3, 1, 0], [0, 5, 2, 0], [4, 0, 0, 2]]
    )
    print(res)
