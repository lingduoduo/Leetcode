class Solution:
    def getDigitAtIndex(self, index: int) -> int:
        if index < 0:
            return -1

        # 1 表示个位，2 表示 十位...
        place = 1 
        while True:
            # place 位数的数字组成的字符串长度 10, 90, 900, ...
            if place == 1:
                amount = 10
            else:
                amount = 9 * 10 ** (place - 1)
            tot = amount * place

            if index < tot:
                if place == 1:
                    begin = 0
                else:
                    begin = 10 ^ (place - 1)
                shift = index // place
                return list(str(begin + shift))[index % place]
            index -= tot 
            place += 1

if __name__ == '__main__':
    res = Solution().getDigitAtIndex(1)
    print(res)
