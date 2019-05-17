'''
S = "abcde"
words = ["a", "bb", "acd", "ace"]
Output: 3
'''
import collections
import bisect


class Solution(object):
    def numMatchingSubseq(self, S, words):
        """
        :type S: str
        :type words: List[str]
        :rtype: int
        """
        ## !! Exceed time limit
        # d = dict()
        # for i in range(len(S)):
        #     d[S[i]] = d.get(S[i], []) + [i]
        d = collections.defaultdict(list)
        for i, s in enumerate(S):
            d[s].append(i)
        
        d2 = set()
        res = 0
        for word in words:
            last_index = -1
            if word in d2:
                res += 1
                continue
            i = 0
            for c in word:
                if c not in d:
                    break
                else:
                    # for pos in d[c]:
                    #     if last_index<pos:
                    #         i+=1
                    #         last_index = pos
                    #         break
                    pos = bisect.bisect_left(d[c], last_index + 1)
                    if pos == len(d[c]):
                        break
                    else:
                        i += 1
                        last_index = d[c][pos]
            
            if i == len(word):
                res += 1
                d2.add(word)
        return res


if __name__ == '__main__':
    S = "abcde"
    words = ["a", "bb", "acd", "ace"]
    result = Solution().numMatchingSubseq(S, words)
    print(result)
    
    S = "acbca"
    # # words = ["a", "bb", "acb", "ace", "ace"]
    words = ["a", "ac"]
    result = Solution().numMatchingSubseq(S, words)
    print(result)
    
    S = "qlhxagxdqh"
    words = ["qlhxagxdq", "qlhxagxdq", "lhyiftwtut", "yfzwraahab"]
    result = Solution().numMatchingSubseq(S, words)
    print(result)
