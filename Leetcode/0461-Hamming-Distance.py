# def Hamming_distince(x, y):
#     result = 0
#     nLoop = max(x, y)
#     while nLoop > 0:
#         bx = x % 2
#         by = y % 2
#         x = x / 2
#         y = y / 2
#         nLoop = max(x, y)
#         if bx != by:
#             result += 1
#     return result


# if __name__ == "__main__":
#     print(Hamming_distince(1, 15))


class Solution:
    def hammingDistance(self, x: int, y: int) -> int:
        return bin(x^y).count('1')

if __name__ == "__main__":
    res = Solution().hammingDistance(1, 15)
    print(res)
    