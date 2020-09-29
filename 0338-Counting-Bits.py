class Solution:
    def countBits(self, num: int):
        if not num:
            return None

        res = [-1]*(1+num)
        res[0] = 0

        for i in range(1, (1+num)):
            if res[i] != -1:
                continue
            j=i
            res[j] = res[j-1]+1 if j%2==1 else res[j-1]
            while j<<2 <= num:
                res[j<<2] = res[j]
                j = j<<2

        return res


if __name__ == '__main__':
    results = Solution().countBits(5)
    print(results)

