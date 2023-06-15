from typing import List
import collections


class Solution:
    def videoStitching(self, clips: List[List[int]], T: int) -> int:
        sclips = sorted(clips, key=lambda x: (x[0], x[1]))

        if sclips[0][0] > 0 or sclips[-1][1] < T:
            return -1

        d = collections.defaultdict(list)
        for k, v in enumerate(clips):
            d[v[1]].append(v)

        for k in d:
            print(sorted(d[k])[-1])

        # stack = [sclips[0]]
        # res = 0
        # while True:
        # 	x0, y0 = stack[-1]


if __name__ == "__main__":
    # clips = clips = [[0,2],[4,6],[8,10],[1,9],[1,5],[5,9]]
    # T = 10
    # res = Solution().videoStitching(clips,  T)
    # print(res)

    # clips = [[0,1],[1,2]]
    # T = 5
    # res = Solution().videoStitching(clips,  T)
    # print(res)

    clips = [
        [0, 1],
        [6, 8],
        [0, 2],
        [5, 6],
        [0, 4],
        [0, 3],
        [6, 7],
        [1, 3],
        [4, 7],
        [1, 4],
        [2, 5],
        [2, 6],
        [3, 4],
        [4, 5],
        [5, 7],
        [6, 9],
    ]
    T = 9
    res = Solution().videoStitching(clips, T)
    print(res)

# 	{1: [[0, 1]], 8: [[6, 8]], 2: [[0, 2]], 6: [[5, 6], [2, 6]], 4: [[0, 4], [1, 4], [3, 4]], 3: [[0, 3], [1, 3]], 7: [[6, 7], [4, 7], [5, 7]], 5: [[2, 5], [4, 5]], 9: [[6, 9]]})
# None
