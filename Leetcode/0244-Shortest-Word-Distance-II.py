###Given a list of words and two words word1 and word2, return the shortest
###distance between these two words in the list.

###For example,
###Assume that words = ["practice", "makes", "perfect", "coding", "makes"].

###Given word1 = “coding”, word2 = “practice”, return 3.
###Given word1 = "makes", word2 = "coding", return 1.

###Note:
###You may assume that word1does not equal toword2, and word1 and word2 are
###both in the list.

###这道题小心重复


class Solution(object):
    def shortestDeistance(self, words, word1, word2):
        d = dict()
        for i in range(len(words)):
            d[words[i]] = d.get(words[i], []) + [i]
        print(d)

        l1 = d[word1]
        l2 = d[word2]

        if len(l1) > len(l2):
            l1, l2 = l2, l1

        res = float("inf")
        for i in l1:
            res = min(res, min([abs(i - j) for j in l2]))

        if res == float("inf"):
            return -1
        else:
            return res


if __name__ == "__main__":
    words = ["practice", "makes", "perfect", "coding", "makes"]
    word1 = "coding"
    word2 = "practice"
    result = Solution().shortestDeistance(words, word1, word2)
    print(result)

    word1 = "makes"
    word2 = "coding"
    result = Solution().shortestDeistance(words, word1, word2)
    print(result)
