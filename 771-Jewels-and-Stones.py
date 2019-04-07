class Solution(object):
    def numJewelsInStones(self, J, S):
        """
        :type J: str
        :type S: str
        :rtype: int
        """
        d = dict()

        for i in range(len(S)):
            d[S[i]] = d.get(S[i], 0) + 1

        res = 0
        for i in range(len(J)):
            if J[i] in d:
                res += d[J[i]]
        return res


if __name__ == '__main__':
    J = "aA"
    S = "aAAbbbb"
    J = "z"
    S = "ZZ"
    result = Solution().numJewelsInStones(J, S)
    print(result)
