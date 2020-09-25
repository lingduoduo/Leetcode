class Solution:
    def maxProduct(self, words) -> int:
        if len(words)<=1:
            return 0

        res = 0

        for i in range(len(words)-1):
            for j in range(i+1, len(words)):
                uncommon = self.uncommonFunc(words[i], words[j])
                res = max(res, uncommon)
        return res

    def uncommonFunc(self, word1, word2):
        n1 = len(word1)
        n2 = len(word2)


        if n1>n2:
            word1 , word2 = word2, word1
            n1, n2 = n2, n1


        for cha in set(word1):
            if cha in set(word2):
                return 0
        return n1*n2
        

class Solution:
    def maxProduct(self, words) -> int:
        res = 0
        d = collections.defaultdict(int)
        N = len(words)
        for i in range(N):
            w = words[i]
            for c in w:
                d[w] |= 1 << (ord(c) - ord('a'))
            for j in range(i):
                if not d[words[j]] & d[words[i]]:
                    res = max(res, len(words[j]) * len(words[i]))
        return res        

if __name__ == '__main__':
    words = ['fddddff', 'abecab']
    results = Solution().uncommonFunc(words[0], words[1])

    # words = ["edadc","ebbfe","aacdde","dfe","cb","fddddff","fabca","adccac","ece","ccaf","feba","bcb","edadc","aea","bacb","acefa","fcebffd","dfeebca","bedcbaa","deaccc","abedc","dadff","eef","ddebbb","abecab","cd","abdeee","eedce","deef","dceaddd","ced","fbbf","ba","eefeda","fb","cddc","adafbf","dded","aadbf","caefbaf","ccebf","dbb","ee","dadcecc","ddbcabb","afeaa","ec","aad","efde","cbcda","cdbdafd","cddc","ecaaa","ae","cfc","bccac","cdcc","abbbf","fcdface","ddbcdc","bfebb","daed","bc","dc","ecdfc","eeb","bb","dad","caecb","fbe","bbbc","cacea","dbc","fbe","bcfffbd","aeda","cff","ddfc","ea","bdfd","ccb","cb","ae","ceabefa","dcea","cbaed","bfedf","fa","ccd","fece","bceef","acabca","dafa","fdeec","dac","cae","adeeadb","ecacc","acfe","de"]
    # results = Solution().maxProduct(words)
    print(results)
