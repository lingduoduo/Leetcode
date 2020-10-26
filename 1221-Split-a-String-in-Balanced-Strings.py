class Solution:
    def balancedStringSplit(self, s: str) -> int:
        r = s.split("L")
        curr = 0
        for i in range(len(r)):
            if r[i] != '':
                r[curr] = r[i]
                curr += 1
        r = r[:curr]
        l = s.split("R")
        curr = 0
        for i in range(len(l)):
            if l[i] != '':
                l[curr] = l[i]
                curr += 1
        l = l[:curr]
        res = []
        print(r)
        print(l)
        
        # while l and r:
        #     while l[0] == '': l.pop(0)
        #     while r[0] == '': r.pop(0)
        #     left = l.pop(0)
        #     right = r.pop(0)
        #     size = min(len(left), len(right))
        #     if s[0] == 'L':
        #         res.append(left[:size]+right[:size])
        #     else:
        #         res.append(right[:size]+left[:size])
        # return len(res)

if __name__ == '__main__':
    # s = "RLRRLLRLRRRL"
    s = "RLLLLRRRLR"
    results = Solution().balancedStringSplit(s)
    print(results)

#     Input: 
# Output: 4
# Explanation: s can be split into "RL", "RRLL", "RL", "RL", each substring contains same number of 'L' and 'R'.