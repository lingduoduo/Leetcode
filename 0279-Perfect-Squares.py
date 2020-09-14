class Solution:
    def numSquares(self, n: int) -> int:
        dp = [float('inf')] * (n+1)
        dp[0] = 0
        for i in range(1, n+1):
            j = 1
            while j*j <= i:
                dp[i] = min(dp[i], dp[i-j*j]+1)
                j += 1
        return dp[-1]


from collections import deque
    q = deque()
    q.append(n)
    count = 0
    while q:
        _q = set()
        for _ in range(len(q)):
            target = q.popleft()
            if target == 0:
                return count
            i = 1
            while i**2 <= target:
                rest = target - i**2
                _q.add(rest)
                i+=1
        count += 1
        q = deque(_q)

