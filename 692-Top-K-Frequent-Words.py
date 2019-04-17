
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
        # d = dict()
        #
        # for i in range(len(words)):
        #     d[words[i]] = d.get(words[i], 0) + 1
        #
        # l = sorted(d.items(), key=lambda x: x[1], reverse = True)
        # d = dict(l)
        # # return [key for i, key in enumerate(d2) if i<k]
        count = collections.Counter(words)
        candidates = count.keys()
        candidates.sort(key= lambda w: (-count[w], w))
        return candidates[:k]

if __name__ == '__main__':
    # words = ["i", "love", "leetcode", "i", "love", "coding"]
    # k=2
    # result = Solution().topKFrequent(words, k)
    # print(result)
    #
    # words = ["the", "day", "is", "sunny", "the", "the", "the", "sunny", "is", "is"]
    # k=4
    # result = Solution().topKFrequent(words, k)
    # print(result)

    words = ["i", "love", "leetcode", "i", "love", "coding"]
    k=2
    result = Solution().topKFrequent(words, k)
    print(result)