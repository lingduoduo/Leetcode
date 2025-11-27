from queue import Queue

class Solution:
    def minimumOperationsToMakeEqual(self, x: int, y: int) -> int:
        q = deque()
        q.append(x)
        res = 0
        dic = {}
        while q:
            for _ in range(len(q)):
                k = q.popleft()
                if k > 1e4 or k < 0:
                    continue
                if k == y:
                    return res
                if k % 11 == 0 and dic.get(k // 11, 0) == 0:
                    dic[k // 11] = 1
                    q.append(k // 11)
                if k % 5 == 0 and dic.get(k // 5, 0) == 0:
                    dic[k // 5] = 1
                    q.append(k // 5)
                if k > 0 and dic.get(k - 1, 0) == 0:
                    dic[k - 1] = 1
                    q.append(k - 1)
                if dic.get(k + 1, 0) == 0:
                    dic[k + 1] = 1
                    q.append(k + 1)
            res += 1
        return res
