from typing import List
class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        result = []
        for i in range(numRows):
            result.append([])
            for j in range(i+1):
                if j in (0, i):
                    result[i].append(1)
                else:
                    result[i].append(result[i-1][j-1]+result[i-1][j])
        return result
class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        result = []
        for i in range(numRows):
            result.append([])
            for j in range(i+1):
                if j in (0, i):
                    result[i].append(1)
                else:
                    result[i].append(result[i-1][j-1]+result[i-1][j])
        return result

class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        res = [[1]]
        for i in range(numRows-1):
            l = res[-1]
            res.append([1] + list(map(sum, zip(l, l[1:]))) + [1])
        return res

if __name__ == "__main__":
    res = Solution().generate(numRows = 5)
    print(res)