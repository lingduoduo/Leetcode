class Solution(object):
    def merge(self, intervals):
        """
        :type intervals: List[List[int]]
        :rtype: List[List[int]]
        [[1,3],[2,6],[8,10],[15,18]]
        """
        if not intervals:
            return False

        res = []

        intervals.sort(key=lambda x: x[0])

        for i in range(len(intervals)):
            if not res or intervals[i][0] > res[-1][1]:
                res.append(intervals[i])
            else:
                num = res.pop()
                start = num[0]
                end = max(num[1], intervals[i][1])
                res.append([start, end])

        return res

if __name__ == '__main__':
    interval = [[1, 3], [2, 6], [8, 10], [15, 18]]
    result = Solution().merge(interval)
    print(result)

    interval = [[1,4],[4,5]]
    result = Solution().merge(interval)
    print(result)