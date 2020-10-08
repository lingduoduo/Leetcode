class Solution:
    def nextGreaterElement(self, n: int) -> int:
        strs = [cha for cha in str(n)]
        if len(strs)==1: return -1
        pos = len(strs) -1
        while pos > 1 and strs[pos-1] >= strs[pos]:
            pos -= 1
        idx1 = pos - 1

        diff = float("inf")
        idx2 = pos
        while pos <= len(strs)-1:
            if (strs[idx1] < strs[pos]) and (diff > (int(strs[pos]) - int(strs[idx1]))):
                diff = int(strs[pos]) - int(strs[idx1])
                idx2 = pos
            pos += 1 
        strs[idx1], strs[idx2] = strs[idx2], strs[idx1]
        res = int(''.join(strs[:idx1+1] + sorted(strs[idx1+1:])))
        if res <= n or res > 2**31 -1: 
            return -1 
        else:
            return res

if __name__ == '__main__':
    # results = Solution().nextGreaterElement(127431)
    results = Solution().nextGreaterElement(1999999999)
    # results = Solution().nextGreaterElement(21)
    # results = Solution().nextGreaterElement(12)
    # results = Solution().nextGreaterElement(198765432)
    
    print(results)
