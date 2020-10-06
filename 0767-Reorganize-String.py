import collections
import heapq
class Solution:
    def reorganizeString(self, S: str) -> str:
        d = collections.Counter(S)
        pq = [(-v, k) for k, v in d.items()]
        heapq.heapify(pq)
        
        if -pq[0][0] > (1+len(S))//2: return ""

        res = []
        while len(pq) >= 2:
            v1, k1 = heapq.heappop(pq)
            v2, k2 = heapq.heappop(pq)
            res.extend([k1, k2])
            if v1 != -1:
                heapq.heappush(pq, (v1 + 1, k1))
            if v2 != -1:
                heapq.heappush(pq, (v2 + 1, k2))
        return "".join(res) + (pq[0][1] if pq else "")         


if __name__ == '__main__':
    # s = "aab"
    s = "vvvlo"
    result = Solution().reorganizeString(s)
    print(result)