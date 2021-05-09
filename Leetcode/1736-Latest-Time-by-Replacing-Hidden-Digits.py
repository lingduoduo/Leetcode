from itertools import product
class Solution:
    def maximumTime(self, time: str) -> str:
        p = {}
        p[0] = []
        p[1] = []
        p[2] = []
        p[3] = []


        if time[0] == "?":
            for num in range(3):
                p[0].append(str(num))
        else:
            p[0].append(time[0])

        if time[1] == "?":
            for num in range(10):
                p[1].append(str(num))
        else:
            p[1].append(time[1])            

        if time[3] == "?":
            for num in range(6):
                p[2].append(str(num))
        else:
            p[2].append(time[3])

        if time[4] == "?":
            for num in range(10):
                p[3].append(str(num))
        else:
            p[3].append(time[4])

        h = 0
        for x, y in product(p[0], p[1]):
            if int(x+y) <= 23:
                h = max(h, int(x+y))
        m = 0
        for x, y in product(p[2], p[3]):
            if int(x+y) <= 59:
                m = max(m, int(x+y))
        hstr = str(h)
        if h < 10:
            hstr = "0" + hstr
        mstr = str(m)
        if m < 10:
            mstr = "0" + mstr
        return hstr + ":" + mstr

if __name__ == '__main__':
    time = "2?:?0"
    res = Solution().maximumTime(time)
    print(res)

    time = "0?:3?"
    res = Solution().maximumTime(time)
    print(res)

    time = "1?:22"
    res = Solution().maximumTime(time)
    print(res)    