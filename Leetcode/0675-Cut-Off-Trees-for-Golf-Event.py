import collections


class Solution:
    def cutOffTree(self, forest) -> int:
        nrow = len(forest)
        ncol = len(forest[0])

        startx = 0
        starty = 0

        d = collections.defaultdict(list)
        d[0] = [(startx, starty)]

        for i in range(nrow):
            for j in range(ncol):
                if forest[i][j] != 0:
                    d[forest[i][j]].append((i, j))

        stack = sorted(d.keys())
        total_steps = 0

        for i in range(len(stack) - 1):
            startx, starty = d[stack[i]][0]
            endx, endy = d[stack[i + 1]][0]

            steps = self.bfs(forest, startx, starty, endx, endy)

            if steps == -1:
                return -1
            total_steps += steps
        return total_steps

    def bfs(self, forest, sr, sc, tr, tc):
        R, C = len(forest), len(forest[0])
        queue = collections.deque([(sr, sc, 0)])
        seen = {(sr, sc)}
        while queue:
            r, c, d = queue.popleft()
            if r == tr and c == tc:
                return d
            for nr, nc in ((r - 1, c), (r + 1, c), (r, c - 1), (r, c + 1)):
                if (
                    0 <= nr < R
                    and 0 <= nc < C
                    and (nr, nc) not in seen
                    and forest[nr][nc]
                ):
                    seen.add((nr, nc))
                    queue.append((nr, nc, d + 1))
        return -1


if __name__ == "__main__":
    # m=[
    #      [1,2,3],
    #      [0,0,4],
    #      [7,6,5]
    #     ]
    # m = [
    #  [1,2,3],
    #  [0,0,0],
    #  [7,6,5]
    # ]
    m = [[2, 3, 4], [0, 0, 5], [8, 7, 6]]
    result = Solution().cutOffTree(m)
    print(result)
