class Solution(object):
    def numJewelsInStones(self, jewels: str, stones: str) -> int:
        jewel_set = set(jewels)
        res = 0
        for stone in stones:
            if stone in jewel_set:
                res += 1
        return res



if __name__ == "__main__":
    J = "aA"
    S = "aAAbbbb"
    J = "z"
    S = "ZZ"
    result = Solution().numJewelsInStones(J, S)
    print(result)
