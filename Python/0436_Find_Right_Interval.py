class Solution:
    def findRightInterval(self, intervals):
        n = len(intervals)

        starts = sorted((interval[0], i) for i, interval in enumerate(intervals))
        res = [-1] * n

        for i, (start, end) in enumerate(intervals):
            l, r = 0, n

            while l < r:
                mid = (l + r) // 2

                if starts[mid][0] >= end:
                    r = mid
                else:
                    l = mid + 1

            if l < n:
                res[i] = starts[l][1]

        return res


if __name__ == "__main__":
    # intervals = [[3,4],[2,3],[1,2]]
    # res = Solution().findRightInterval(intervals)
    # print(res)

    # intervals = [[1,4],[2,3],[3,4]]
    # res = Solution().findRightInterval(intervals)
    # print(res)

    intervals = [[1, 12], [2, 9], [3, 10], [13, 14], [15, 16], [16, 17]]
    res = Solution().findRightInterval(intervals)
    print(res)
