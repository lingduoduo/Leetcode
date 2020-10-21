class Solution:
    def removeCoveredIntervals(self, intervals) -> int:

        intervals.sort(key = lambda x: (x[0],-x[1]))
        res = 0
        print(intervals)

        for i in range(len(intervals)):
            if i == 0: 
                x0, y0 = intervals[i]
                res += 1
            else:
                x1, y1 = intervals[i]
                if y1 <= y0:
                    continue
                else:
                    x0 = x1
                    y0 = y1
                    res += 1
        return res

if __name__ == '__main__':
    # intervals = [[1,4],[3,6],[2,8]]
    # intervals = [[1,4],[2,3]]
    # intervals =  [[0,10],[5,12]]
    # intervals = [[3,10],[4,10],[5,11]]
    intervals = [[1,2],[1,4],[3,4]]
    results = Solution().removeCoveredIntervals(intervals)
    print(results)


# Input: intervals = [[1,2],[1,4],[3,4]]
# Output: 1

