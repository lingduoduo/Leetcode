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
        ###first try
        ###count = collections.Counter(words)
        ###candidates = count.keys()
        ###candidates.sort(key=lambda w: (-count[w], w))
        ###return candidates[:k]
        
        ######second try
        ###d = dict()
        ###for i in range(len(words)):
        ###    d[words[i]] = d.get(words[i], 0) + 1
        
        ###d2 = dict()
        ###for key, v in d.items():
        ###    if v not in d2:
        ###        d2[v] = [key]
        ###    else:
        ###        d2[v] += [key]
        ###    d2[v] = sorted(d2[v])
        
        ###res = []
        ###for key in sorted(d2.keys(), reverse=True):
        ###    res += d2[key]
        ###return res[:k]
        
        ######third try
        ###d = dict()
        ###for i in range(len(words)):
        ###    d[words[i]] = d.get(words[i], 0) + 1
        
        ###def comp(x, y):
        ###    if x[1] == y[1]:
        ###        return cmp(x[0], y[0])
        ###    else:
        ###        return -cmp(x[1], y[1])
        
        ###return [x[0] for x in sorted(d.items(), cmp=comp)[:k]]
        
        ######Fouth try
        ###d = dict()
        ###for i in range(len(words)):
        ###    d[words[i]] = d.get(words[i], 0) + 1
        ###heap = [(-freq, word) for word, freq in d.items()]
        ###heapq.heapify(heap)
        ###return [heapq.heappop(heap)[1] for _ in range(k)]


        ###fifth try
        count = collections.Counter(words)
        count = {k: v for k, v in sorted(count.items(), key=lambda x: (-x[1], x[0]))}
        candidates = list(count.keys())
        return candidates[:k]

if __name__ == '__main__':
    words = ["i", "love", "leetcode", "i", "love", "coding"]
    k = 2
    result = Solution().topKFrequent(words, k)
    print(result)
    #
    words = [
        "the",
        "day",
        "is",
        "sunny",
        "the",
        "the",
        "the",
        "sunny",
        "is",
        "is"]
    k = 4
    result = Solution().topKFrequent(words, k)
    print(result)
    
    words = ["aaa", "aa", "a"]
    k = 1
    result = Solution().topKFrequent(words, k)
    print(result)
