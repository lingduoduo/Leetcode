class Solution:
    def maxRepeating(self, sequence: str, word: str) -> int:
        # res = 0
        # i = 0
        # j = 0
        # while i < len(sequence) and j < len(word):
        #     if sequence[i] != word[j]:
        #         i += 1
        #         j = 0
        #     while i < len(sequence) and j < len(word) and sequence[i] == word[j]:
        #         i += 1
        #         j += 1
        #     if j == len(word):
        #         res += 1
        #         j = 0
        # return res

        res = 0
        j = 0
        i = 0
        # Iterate through the entire seqeunce
        while i < len(sequence):
            # Found a match
            if word == sequence[i:i+len(word)]:
                j += 1
                res += 1
                i += len(word)
            # Didn't find a match
            else:
                j = 0
                i += 1
        return res


        # newstr = sequence.replace(word, "#")
        # print(newstr)
        # res = newstr.count("#")
        # return res


if __name__ == '__main__':
    sequence = "ababc"
    word = "ab"
    res = Solution().maxRepeating(sequence, word)
    print(res)

    sequence = "ababc"
    word = "ba"
    res = Solution().maxRepeating(sequence, word)
    print(res)

    sequence = "ababc"
    word = "ac"
    res = Solution().maxRepeating(sequence, word)
    print(res)

    sequence = "aaaba aaab aaaba aaaba aaaba aaaba aaaba"
    word = "aaaba"
    res = Solution().maxRepeating(sequence, word)
    print(res)