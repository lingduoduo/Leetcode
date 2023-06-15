# class Solution:
#     '''
#     Input: n = 4, k = 2
#     Output:
#     [
#       [2,4],
#       [3,4],
#       [2,3],
#       [1,2],
#       [1,3],
#       [1,4],
#     ]
#     '''
class Solution:
    def combine(self, n: int, k: int):
        res = []

        for s in range(1 << n):
            tmp = []
            for i in range(n):
                if str(bin(s)).count("1") == k and s & 1 << i > 0:
                    tmp.append(i + 1)
            if len(tmp) > 0:
                res.append(tmp)
        return res


class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        def backtrack(first=1, curr=[]):
            # if the combination is done
            if len(curr) == k:
                output.append(curr[:])
            for i in range(first, n + 1):
                # add i into the current combination
                curr.append(i)
                # use next integers to complete the combination
                backtrack(i + 1, curr)
                # backtrack
                curr.pop()

        output = []
        backtrack()
        return output


if __name__ == "__main__":
    n = 5
    k = 3
    result = Solution().combine(n, k)
    print(result)
