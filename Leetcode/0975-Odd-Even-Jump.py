from typing import List

class Solution:
    def oddEvenJumps(self, arr: List[int]) -> int:
        
		# find next index of current index that is the least larger/smaller
        def getNextIndex(sortedIdx):
            stack = []
            result = [None] * len(sortedIdx)
        
            for i in sortedIdx:
                while stack and i > stack[-1]:
                    result[stack.pop()] = i
                stack.append(i)
            return result
        
        sortedIdx = sorted(range(len(arr)), key= lambda x: arr[x])
        oddIndexes = getNextIndex(sortedIdx)
        sortedIdx.sort(key=lambda x: -arr[x])
        evenIndexes = getNextIndex(sortedIdx)
        
		# [odd, even], the 0th jump is even
        dp = [[0,1] for _ in range(len(arr))]
        
        for i in range(len(arr)):
            if oddIndexes[i] is not None:
                dp[oddIndexes[i]][0] += dp[i][1]
            if evenIndexes[i] is not None:
                dp[evenIndexes[i]][1] += dp[i][0]
				
        return dp[-1][0] + dp[-1][1]

if __name__ == "__main__":
    res = Solution().oddEvenJumps(arr = [10,13,12,14,15])
    print(res)