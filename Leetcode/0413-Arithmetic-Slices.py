import copy
class Solution:
    def numberOfArithmeticSlices(self, A) -> int:
        count = 0
        addend = 0
        for i in range(len(A) - 2):
            if A[i + 1] - A[i] == A[i + 2] - A[i + 1]:
                addend += 1
                count += addend
            else:
                addend = 0
        return count
                
                
                
if __name__ == '__main__':
    A = [1, 2, 3, 4, 5, 6]
    # A = [7, 7, 7, 7]
    res = Solution().numberOfArithmeticSlices(A)
    print(res)