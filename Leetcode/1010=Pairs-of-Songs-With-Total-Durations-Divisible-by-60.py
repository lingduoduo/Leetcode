import itertools
import collections
class Solution:
    def numPairsDivisibleBy60(self, time) -> int:

        # d = collections.defaultdict(list)
        # res = set()
        # for i in range(len(time)):
        #     d[time[i] % 60].append(i)
        
        # for i in range(len(time)):
        #     if 60 - time[i] % 60 in d and i not in d[60 - time[i] % 60]:
        #         if i < d[60 - time[i] % 60]:
        #             res.add((d[60 - time[i] % 60], i))
        #         else:
        #             res.add((i, d[60 - time[i] % 60]))
        
        # cnt = [x%60==0 for x in time].count(True)   
        # return len(res) + cnt * (cnt-1)//2


        record = [0 for _ in range(0, 60)]
        for index, item in enumerate(time):
            record[item % 60] += 1
        
        res = 0
        for i in range(0, len(time)):
            temp = time[i] % 60
 
            if temp:
                record[temp] -= 1
                res += record[60 - temp]
            elif temp == 0 and record[0] > 1:
                # print res, record[0]
                # 5 4+3 +2 +1
                res += record[0] * (record[0] - 1) // 2
                record[0] = 0
 
        return res


        # pairs = itertools.combinations(time, 2)
        # cnt = [(x+y)%60 == 0 for x,y in pairs].count(True)
        # return cnt

if __name__ == '__main__':
    time = [269,230,318,468,171,158,350,60,287,27,11,384,332,267,412,478,280,303,242,378,129,131,164,467,345,146,264,332,276,479,284,433,117,197,430,203,100,280,145,287,91,157,5,475,288,146,370,199,81,428,278,2,400,23,470,242,411,470,330,144,189,204,62,318,475,24,457,83,204,322,250,478,186,467,350,171,119,245,399,112,252,201,324,317,293,44,295,14,379,382,137,280,265,78,38,323,347,499,238,110,18,224,473,289,198,106,256,279,275,349,210,498,201,175,472,461,116,144,9,221,473]
    result = Solution().numPairsDivisibleBy60(time)
    print(result)