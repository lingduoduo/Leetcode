from typing import List


class Solution:
    def shiftGrid(self, grid: List[List[int]], k: int) -> List[List[int]]:
        k = k % (len(grid) * len(grid[0]))
        if k == 0:
            return grid
        nums = []
        for row in grid:
            for element in row:
                nums.append(element)
        nums = nums[-k:] + nums[:-k]
        print(nums)
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                # print(f"{i, j, nums[i*len(grid[0]) + j]}")
                grid[i][j] = nums[i * len(grid[0]) + j]
        return grid


if __name__ == "__main__":
    grid = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
    k = 1
    res = Solution().shiftGrid(grid, k)
    print(f"{res}")

    grid = [[3, 8, 1, 9], [19, 7, 2, 5], [4, 6, 11, 10], [12, 0, 21, 13]]
    k = 4
    res = Solution().shiftGrid(grid, k)
    print(f"{res}")

    grid = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
    k = 9
    res = Solution().shiftGrid(grid, k)
    print(f"{res}")

    grid = [[1], [2], [3], [4], [7], [6], [5]]
    k = 23
    res = Solution().shiftGrid(grid, k)
    print(f"{res}")
