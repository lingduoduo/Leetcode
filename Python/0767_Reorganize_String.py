import collections
import heapq


class Solution:
    def reorganizeString(self, S: str) -> str:
        d = collections.Counter(S)

        max_heap = [(-freq, char) for char, freq in d.items()]
        heapq.heapify(max_heap)

        res = []
        while len(max_heap) >= 2:
            freq1, char1 = heapq.heappop(max_heap)
            freq2, char2 = heapq.heappop(max_heap)

            res.extend([char1, char2])
            if freq1 + 1 < 0:
                heapq.heappush(max_heap, (freq1 + 1, char1))
            if freq2 + 1 < 0:
                heapq.heappush(max_heap, (freq2 + 1, char2))

        if max_heap:
            freq, char = heapq.heappop(max_heap)
            if -freq > 1:
                return ""
            res.append(char)

        return "".join(res)


if __name__ == "__main__":
    # s = "aab"
    s = "vvvlo"
    result = Solution().reorganizeString(s)
    print(result)
