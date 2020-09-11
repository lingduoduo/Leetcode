class Solution(object):
    def insert(self, intervals, newInterval):
        """
        :type intervals: List[List[int]]
        :type newInterval: List[int]
        :rtype: List[List[int]]
        """
        ###Method 1
        intervals.append(newInterval)
        intervals.sort(key=lambda x: x[0])

        res = []
        for i in range(len(intervals)):
            if not res or intervals[i][0] > res[-1][1]:
                res.append(intervals[i])
            else:
                num = res.pop()
                end = max(num[1], intervals[i][1])
                res.append([num[0], end])

        return res


if __name__ == '__main__':
    intervals = [[1, 3], [6, 9]]
    newInterval = [2, 5]
    result = Solution().insert(intervals, newInterval)
    print(result)

    intervals = [[1, 2], [3, 5], [6, 7], [8, 10], [12, 16]]
    newInterval = [4, 8]
    result = Solution().insert(intervals, newInterval)
    print(result)

    intervals = [[1, 5]]
    ###newInterval = [2,3]
    newInterval = [0, 3]
    result = Solution().insert(intervals, newInterval)
    print(result)
