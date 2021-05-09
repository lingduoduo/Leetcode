import collections
class Solution:
    def countBalls(self, lowLimit: int, highLimit: int) -> int:
        res = 0
        d = {}
        for i in range(lowLimit, highLimit+1):
            tmp = i
            part = 0
            while tmp > 0:
                part += tmp % 10
                tmp = tmp //10
            d[part] = d.get(part, 0) + 1

        return max(d.values())



if __name__ == '__main__':
    res = Solution().countBalls(1, 10)
    res = Solution().countBalls(5, 15)
    res = Solution().countBalls(19, 28)
    print(res)