class Solution:
    def canFormArray(self, arr: List[int], pieces: List[List[int]]) -> bool:
        d = {}
        for i in range(len(pieces)):
            num = pieces[i][0]
            if num not in arr:
                continue
            elif arr.index(num) >= 0:
                d[num] = i

        res = []
        for num in arr:
            if num in d:
                res += pieces[d[num]]
        return res == arr


if __name__ == "__main__":
    arr = [85]
    pieces = [[85]]
    res = Solution().canFormArray(arr, pieces)
    print(res)

    arr = [15, 88]
    pieces = [[88], [15]]
    res = Solution().canFormArray(arr, pieces)
    print(res)

    arr = [91, 4, 64, 78]
    pieces = [[78], [4, 64], [91]]
    res = Solution().canFormArray(arr, pieces)
    print(res)

    arr = [75, 1, 60, 91, 84, 55, 5, 39, 19, 52, 38, 66, 14, 17, 49]
    pieces = [
        [60],
        [52, 38],
        [66],
        [39],
        [19],
        [1],
        [84, 55],
        [17],
        [14],
        [49],
        [91],
        [5],
        [75],
    ]
    res = Solution().canFormArray(arr, pieces)
    print(res)
