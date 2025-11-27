class Solution:
    def prisonAfterNDays(self, cells, N: int):
        if N % 14 == 0:
            N = 14
        else:
            N = N % 14
        for i in range(N):
            prev = cells[::]
            for j in range(1, len(cells) - 1):
                if (prev[j - 1] == prev[j + 1]) or (prev[j - 1] == prev[j + 1]):
                    cells[j] = 1
                else:
                    cells[j] = 0
                cells[0] = 0
                cells[-1] = 0
            print([i, cells])
        return cells


if __name__ == "__main__":
    cells = [0, 1, 0, 1, 1, 0, 0, 1]
    N = 1
    results = Solution().prisonAfterNDays(cells, N)
    print(results)


# Day 0: [0, 1, 0, 1, 1, 0, 0, 1]
# Day 1: [0, 1, 1, 0, 0, 0, 0, 0]
# Day 2: [0, 0, 0, 0, 1, 1, 1, 0]
# Day 3: [0, 1, 1, 0, 0, 1, 0, 0]
# Day 4: [0, 0, 0, 0, 0, 1, 0, 0]
# Day 5: [0, 1, 1, 1, 0, 1, 0, 0]
# Day 6: [0, 0, 1, 0, 1, 1, 0, 0]
# Day 7: [0, 0, 1, 1, 0, 0, 0, 0]
