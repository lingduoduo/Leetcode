class Solution:
    def isAlienSorted(self, words, order) -> bool:
        d = {}
        d = {c : i for i, c in enumerate(order)}
        
        for i in range(1, len(words)):
            j = 0
            if words[i-1] == words[i]:
                continue
            length = min(len(words[i-1]), len(words[i]))
            while j < length and d[words[i-1][j]] == d[words[i][j]]:
                j += 1
            if j < length and d[words[i-1][j]] <= d[words[i][j]]:
                continue
            elif j < length and d[words[i-1][j]] > d[words[i][j]]:
                return False
            else:
                if len(words[i-1]) < len(words[i]):
                    continue
                else:
                    return False
        return True

class Solution:
    def isAlienSorted(self, words: List[str], order: str) -> bool:
        d = {c : i for i, c in enumerate(order)}
        t_words = []
        for i in range(len(words)):
            l = [d[w] for w in words[i]]
            t_words.append(l)
        return sorted(t_words) == t_words

if __name__ == '__main__':
    words = ["hello", "leetcode"]
    order = "hlabcdefgijkmnopqrstuvwxyz"
    results = Solution().isAlienSorted(words, order)
    print(results)
