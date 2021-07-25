class Solution:
    def getLucky(self, s: str, k: int) -> int:
        '''For example, if s = "zbax" and k = 2, then the resulting integer would be 8 by the following operations:

            Convert: "zbax" ➝ "(26)(2)(1)(24)" ➝ "262124" ➝ 262124
            Transform #1: 262124 ➝ 2 + 6 + 2 + 1 + 2 + 4 ➝ 17
            Transform #2: 17 ➝ 
        '''
        tmp = ''
        for cha in s:
            num = ord(cha) - ord('a') + 1
            tmp += str(num)

        res = 0
        for i in range(k): 
            res = 0
            for cha in tmp:
                res += int(cha)
            tmp = str(res)
        return res        

if __name__ == '__main__':
    # res = Solution().getLucky(s="zbax",  k=2)
    # print(res)

    res = Solution().getLucky(s="iiii",  k=1)
    print(res)
