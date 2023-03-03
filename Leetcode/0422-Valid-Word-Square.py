from typing import List
class Solution:
    def validWordSquare(self, words: List[str]) -> bool:
        for word_num in range(len(words)):
            for char_pos in range(len(words[word_num])):
                # char_pos (curr 'row' word) is bigger than column word, or
                # word_num (curr 'column' word) is bigger than row word, or
                # characters at index (word_num,char_pos) and (char_pos,word_num) are not equal.
                if char_pos >= len(words) or \
                        word_num >= len(words[char_pos]) or \
                        words[word_num][char_pos] != words[char_pos][word_num]:
                    return False
        return True

if __name__ == "__main__":
    # res = Solution().validWordSquare(words=["abcd","bnrt","crmy","dtye"])
    # print(res)
    #
    # res = Solution().validWordSquare(words = ["ball","area","read","lady"])
    # print(res)

    # res = Solution().validWordSquare(words = ["abcd","bnrt","crm","dt"])
    # print(res)

    # res = Solution().validWordSquare(words = ["abcd","bnrt","crm","dt"])
    # print(res)
    res = Solution().validWordSquare(words = ["ball", "asee", "lett", "le"])
    print(res)