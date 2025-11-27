class Solution:
    def minimumAbsDifference(self, arr):
        arr = sorted(arr)
        res = []
        for i in range(1, len(arr)):
            if len(res) == 0:
                res = [[arr[i - 1], arr[i]]]
                minabs = arr[i] - arr[i - 1]
            elif arr[i] - arr[i - 1] == minabs:
                res.append([arr[i - 1], arr[i]])
            elif arr[i] - arr[i - 1] < minabs:
                res = [[arr[i - 1], arr[i]]]
                minabs = arr[i] - arr[i - 1]
        return res


if __name__ == "__main__":
    arr = [3, 8, -10, 23, 19, -4, -14, 27]
    res = Solution().minimumAbsDifference(arr)
    print(res)
