import collections


class Solution:
    def relativeSortArray(self, arr1, arr2):
        d = collections.Counter(arr1)
        print(d)

        res = []
        for i in range(len(arr2)):
            res = res + [arr2[i]] * d[arr2[i]]

        res2 = []
        for k in d:
            if k not in res:
                res2 = res2 + [k] * d[k]
        return res + sorted(res2)


# [2,21,43,38,0,42,33,7,24,13,12,27,12,24,5,23,29,48,30,31]
# [2,42,38,0,43,21]
if __name__ == "__main__":
    arr1 = [2, 21, 43, 38, 0, 42, 33, 7, 24, 13, 12, 27, 12, 24, 5, 23, 29, 48, 30, 31]
    arr2 = [2, 42, 38, 0, 43, 21]
    results = Solution().relativeSortArray(arr1, arr2)
    print(results)
