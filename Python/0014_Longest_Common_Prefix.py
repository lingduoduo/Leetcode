from typing import List


class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        # this will be an answer
        pref = ""
        # find min and max words among strs
        minWord = min(strs)
        maxWord = max(strs)

        # for iteration
        i = 0
        n = min(len(minWord), len(maxWord))

        while i < n:
            # if chars are equal
            if minWord[i] == maxWord[i]:
                # add this char to the answer
                pref += minWord[i]
            else:
                # if not, break
                break
            i += 1

        return pref


class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        res = ""
        for a in zip(*strs):
            if len(set(a)) == 1:
                res += a[0]
            else:
                return res
        return res


if __name__ == "__main__":
    strs = ["flower", "flow", "flight"]
    ###strs = ["aa","a"]
    ###strs = ["dog","racecar","car"]
    results = Solution().longestCommonPrefix(strs)
    print(results)
