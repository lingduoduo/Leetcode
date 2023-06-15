import collections


class Solution:
    def shortestSubarray(self, A, K: int) -> int:
        n = len(A)
        presum = [0] * (1 + n)
        for i in range(n):
            presum[1 + i] += presum[i] + A[i]
        res = float("inf")
        q = collections.deque()
        q.append(0)
        for idx in range(1, 1 + n):
            while q and presum[idx] - presum[q[0]] >= K:
                res = min(res, idx - q[0])
                q.popleft()
            while q and presum[idx] < presum[q[-1]]:
                q.pop()
            q.append(idx)
        return -1 if res == float("inf") else res


if __name__ == "__main__":
    A = [1]
    K = 1
    res = Solution().shortestSubarray(A, K)
    print(res)

    A = [1, 2]
    K = 4
    res = Solution().shortestSubarray(A, K)
    print(res)

    A = [2, -1, 2]
    K = 3
    res = Solution().shortestSubarray(A, K)
    print(res)
