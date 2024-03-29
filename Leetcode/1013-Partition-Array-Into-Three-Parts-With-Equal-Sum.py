class Solution(object):
    def canThreePartsEqualSum(self, A):
        """
        :type A: List[int]
        :rtype: bool
        Input: [0,2,1,-6,6,-7,9,1,2,0,1]
        Output: true
        Explanation: 0 + 2 + 1 = -6 + 6 - 7 + 9 + 1 = 2 + 0 + 1

        Input: [0,2,1,-6,6,7,9,-1,2,0,1]
        Output: false

        Input: [3,3,6,5,-2,2,5,1,-9,4]
        Output: true
        Explanation: 3 + 3 = 6 = 5 - 2 + 2 + 5 + 1 - 9 + 4

        """
        if sum(A) % 3 != 0:
            return False

        target = sum(A) / 3
        cnt = 0
        par = 0
        for i in range(len(A)):
            par += A[i]
            if par == target:
                cnt += 1
                par = 0
        if cnt == 3:
            return True
        else:
            return False


if __name__ == "__main__":
    A = [1, 1, 1]
    result = Solution().canThreePartsEqualSum(A)
    print(result)

    A = [0, 2, 1, -6, 6, -7, 9, 1, 2, 0, 1]
    result = Solution().canThreePartsEqualSum(A)
    print(result)

    A = [0, 2, 1, -6, 6, 7, 9, -1, 2, 0, 1]
    result = Solution().canThreePartsEqualSum(A)
    print(result)

    A = [3, 3, 6, 5, -2, 2, 5, 1, -9, 4]
    result = Solution().canThreePartsEqualSum(A)
    print(result)

    A = [
        7992,
        -1996,
        -3772,
        4926,
        2430,
        -2506,
        -5496,
        -598,
        7824,
        -6202,
        4,
        2948,
        -5095,
        8450,
        -3451,
        -3805,
        3340,
        -307,
        -2340,
        2906,
        3526,
        1158,
        -7363,
        -56,
        -803,
        -165,
        1191,
        3504,
        -48,
        -5221,
        1410,
        124,
        983,
        -2210,
        5543,
        -3680,
        1432,
        -848,
        -3048,
        3423,
        1904,
        -3640,
        -284,
        -446,
        907,
        5213,
        -4182,
        -2233,
        4490,
        -118,
        -5645,
        1053,
        -316,
        -149,
        6215,
        -2366,
        -1998,
        -1701,
        7931,
        -6324,
        5020,
        -5264,
        1452,
        5213,
        -8356,
        3838,
        -870,
        5491,
        -8553,
        8895,
        -3272,
        -3431,
        1967,
        -1486,
        -1752,
        4113,
        3341,
        -1150,
        -5170,
        7388,
        -3084,
        1130,
        -3595,
        1195,
        -3126,
        5347,
        -4656,
        -1875,
        -151,
        4429,
        155,
        -910,
        -3966,
        1529,
        -320,
        -1101,
        1102,
        3027,
        -3313,
        6764,
        -7363,
        7538,
        -3081,
        -2129,
        2926,
        -6038,
        2978,
        -936,
        73,
        6307,
        818,
        -155,
        -8741,
        4828,
        2804,
        -2577,
        -3982,
        1232,
        -1033,
        6376,
        -6625,
        1154,
        6427,
        -8643,
        19,
        3210,
        5633,
        -6729,
        -1869,
        1620,
        3426,
        -3699,
        271,
        3356,
        33,
        -1439,
        -1251,
        3767,
        -453,
        1601,
        -6860,
        317,
        3694,
        -3996,
        493,
        3488,
        1211,
        2436,
        419,
        -5461,
        3875,
        -5213,
        1877,
        2321,
        -388,
        -5323,
        8490,
        -412,
        -1238,
        2057,
        -5331,
        -1943,
        3433,
        377,
        -5959,
        4559,
        2230,
        -407,
        -830,
        -435,
        -3724,
        690,
        6494,
        -6304,
        -383,
        5326,
        -257,
        -3057,
        2387,
        -2207,
        -1930,
        174,
        139,
        -1870,
        1163,
        7409,
        -4667,
        -3919,
        2683,
        -3256,
        8,
    ]
    result = Solution().canThreePartsEqualSum(A)
    print(result)
