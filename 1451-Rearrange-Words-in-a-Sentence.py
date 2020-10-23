class Solution:
    def arrangeWords(self, text: str) -> str:
        words = text.split(" ")

        d = collections.defaultdict(list)
        for idx, word in enumerate(words):
            if idx == 0:
                d[len(word)].append(word.lower())
            else:
                d[len(word)].append(word)

        d_sorted = sorted(d.items(), key = lambda x: x[0]) 
        res = []
        for k, v in d_sorted:
            res += v

        res_adjust = ' '.join(res)
        return res_adjust[0].upper() + res_adjust[1:]

if __name__ == '__main__':
    # text = "Leetcode is cool"
    text = "To be or not to be"
    results = Solution().arrangeWords(text)
    print(results)

# "To be or to be not"