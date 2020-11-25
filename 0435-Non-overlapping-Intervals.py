class Solution:
    def eraseOverlapIntervals(self, intervals) -> int:
        if not intervals:
            return 0
        
        s_intervals = sorted(intervals, key=lambda x: (x[0], x[1]))

        res = 0
        
        stack = [s_intervals[0]]
        
        for x, y in s_intervals[1:]:
            x0, y0 = stack[-1]

            if y0 <= x:
                stack.append([x, y])
            else:
                if y < y0:
                    stack.pop()
                    stack.append([x, y])
                res += 1
        return res

if __name__ == '__main__':
    intervals = [[1,2],[2,3],[3,4],[1,3]]
    res = Solution().eraseOverlapIntervals(intervals)
    print(res)
    intervals = [[1,2],[1,2],[1,2]]
    res = Solution().eraseOverlapIntervals(intervals)
    print(res)
    intervals = [[1,2],[2,3]]
    res = Solution().eraseOverlapIntervals(intervals)
    print(res)
    intervals = [[1,100],[11,22],[1,11],[2,12]]
    res = Solution().eraseOverlapIntervals(intervals)
    print(res)

    # intervals = [[0,2],[1,3],[2,4],[3,5],[4,6]]
    res = Solution().eraseOverlapIntervals(intervals)
    print(res)