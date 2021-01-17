# class Solution:
#     def balancedStringSplit(self, s: str) -> int:
#         r = s.split("L")
#         curr = 0
#         for i in range(len(r)):
#             if r[i] != '':
#                 r[curr] = r[i]
#                 curr += 1
#         r = r[:curr]
#         l = s.split("R")
#         curr = 0
#         for i in range(len(l)):
#             if l[i] != '':
#                 l[curr] = l[i]
#                 curr += 1
#         l = l[:curr]
#         return min(len(l), len(r))
        
class Solution:
    def balancedStringSplit(self, s: str) -> int:
        res = 0
        l, r = 0, 0
        for i in list(s):
            print([i, l, r, res])
            if i == 'L':
                l += 1
            else:
                r += 1
            if l == r:
                res += 1
                l = r = 0
        return res
        

if __name__ == '__main__':
    # s = "RLRRLLRLRL"
    # s = "RLLLLRRRLR"
    s = "LLLLRRRR"
    results = Solution().balancedStringSplit(s)
    print(results)

#     Input: 
# Output: 4
# Explanation: s can be split into "RL", "RRLL", "RL", "RL", each substring contains same number of 'L' and 'R'.