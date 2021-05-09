class Solution:
    def maxDistToClosest(self, seats) -> int:
        i = 0
        while i < len(seats) and seats[i] == 0:
            i += 1
        left = i

        zeros = cur = 0
        for i in range(left, len(seats)):
            if seats[i]:
                zeros = max(zeros, cur)
                cur = 0
            else:
                cur += 1
        res = max(left, (zeros + 1) // 2, cur)
        return res



if __name__ == '__main__':
    seats = [1,0,0,0,0,1,0,1]
    res = Solution().maxDistToClosest(seats)
    print(res)

