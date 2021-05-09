from typing import List
class Solution:
    def spellchecker(self, wordlist: List[str], queries: List[str]) -> List[str]:
        wordset = set(wordlist)
        lower_d = {}
        vowel_d = {}
        for w in wordlist:
            w_lower = w.lower()
            if w_lower not in lower_d:
                lower_d[w_lower] = w
            tmp = ''.join(['#' if c in 'aeiou' else c for c in w_lower])
            if tmp not in vowel_d:
                vowel_d[tmp] = w
        res = []
        for q in queries:
            if q in wordset:
                res.append(q)
                continue
            w_lower = q.lower()
            if w_lower in lower_d:
                res.append(lower_d[w_lower])
                continue
            tmp = ''.join(['#' if c in 'aeiou' else c for c in w_lower])
            if tmp in vowel_d:
                res.append(vowel_d[tmp])
                continue
            res.append("")
        return res

if __name__ == '__main__':
    wordlist = ["KiTe","kite","hare","Hare"]
    queries = ["kite","Kite","KiTe","Hare","HARE","Hear","hear","keti","keet","keto"]
    res = Solution().spellchecker(wordlist, queries)
    print(res)
