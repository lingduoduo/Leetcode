import collections


class Solution(object):
    def topKFrequent(self, words, k):
        """
        :type words: List[str]
        :type k: int
        :rtype: List[str]
        ["i", "love", "leetcode", "i", "love", "coding"]
        k = 2
        """
        count = collections.Counter(words)
        count = {k: v for k, v in sorted(count.items(), key=lambda x: (-x[1], x[0]))}
        candidates = list(count.keys())
        return candidates[:k]


class Pair:
    def __init__(self, word, freq):
        self.word = word
        self.freq = freq

    def __lt__(self, p):
        return self.freq < p.freq or (self.freq == p.freq and self.word > p.word)


class Solution:
    def topKFrequent(self, words: List[str], k: int) -> List[str]:
        cnt = Counter(words)
        stack = []

        for i, v in cnt.items():
            heapq.heappush(stack, Pair(i, v))
            if len(stack) > k:
                heapq.heappop(stack)

        return [p.word for p in sorted(stack, reverse=True)]


if __name__ == "__main__":
    words = ["i", "love", "leetcode", "i", "love", "coding"]
    k = 2
    result = Solution().topKFrequent(words, k)
    print(result)
    #
    words = ["the", "day", "is", "sunny", "the", "the", "the", "sunny", "is", "is"]
    k = 4
    result = Solution().topKFrequent(words, k)
    print(result)

    words = ["aaa", "aa", "a"]
    k = 1
    result = Solution().topKFrequent(words, k)
    print(result)
