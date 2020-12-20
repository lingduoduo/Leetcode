from itertools import permutations
import bisect
class Solution:
    def canFormArray(self, arr, pieces) -> bool:
        pp = pieces.copy()
        for i in range(len(pieces)):
            if len(pieces[i]) == 1:
                pp.remove(pieces[i])
                arr.remove(pieces[i][0])
        if not arr:
            return True
        l = permutations(pp, len(pp)) 
        for p in l:
            i = 0
            res = []
            while i < len(p):
                res += p[i]
                i += 1
            if res == arr:
                return True
        return False

if __name__ == '__main__':
    # arr = [85]
    # pieces = [[85]]
    # res = Solution().canFormArray(arr, pieces)
    # print(res)

    # arr = [15,88]
    # pieces = [[88],[15]]
    # res = Solution().canFormArray(arr, pieces)
    # print(res)

    arr = [91,4,64,78]
    pieces = [[78],[4,64],[91]]
    res = Solution().canFormArray(arr, pieces)
    print(res)

    # arr = [75,1,60,91,84,55,5,39,19,52,38,66,14,17,49]
    # pieces = [[60],[52,38],[66],[39],[19],[1],[84,55],[17],[14],[49],[91],[5],[75]]
    # res = Solution().canFormArray(arr, pieces)
    # print(res)
