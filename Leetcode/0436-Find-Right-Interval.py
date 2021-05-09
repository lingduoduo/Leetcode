class Solution:
    def findRightInterval(self, intervals):
        res = [-1]*len(intervals)
        d = {}
        for idx, val in enumerate(intervals):
            d[val[0], val[1]] = idx
        
        s = sorted(intervals, key = lambda x: (x[1], x[0]))
        x0, y0 = s[0]

        for x1, y1 in s[1:]:
            if y0 <= x1:
                res[d[x0, y0]] = d[x1, y1]
                x0 = x1
                y0 = y1
            elif y1 < y0:
                x0 = x1
                y0 = y1

        return res

if __name__ == '__main__':
    # intervals = [[3,4],[2,3],[1,2]]
    # res = Solution().findRightInterval(intervals)
    # print(res)

    # intervals = [[1,4],[2,3],[3,4]]
    # res = Solution().findRightInterval(intervals)
    # print(res)

    intervals = [[1,12],[2,9],[3,10],[13,14],[15,16],[16,17]]
    res = Solution().findRightInterval(intervals)
    print(res)