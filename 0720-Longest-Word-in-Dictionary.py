class Solution(object):
    def longestWord(self, words):
        """
        :type words: List[str]
        :rtype: str
        """
        # curr = sorted(words)
        
        # result = ""
        
        # for curr in words:
        #     isIn = True
        #     for i in range(1, len(curr)):
        #         if curr[:i] not in words:
        #             isIn = False
        #             break
        #     if isIn:
        #         if not result or len(result) < len(curr):
        #             result = curr
        #         elif len(curr) == len(result) and result > curr:
        #             result = curr
        # return result

        res = []
        curr = sorted(words)[::-1]
        d = set(words)

        for word in curr:
            found = True
            for i in range(1, len(word)):
                print(word[:i])
                if word[:i] not in d:
                    found = False
                    break
            if found:
                if len(res)==0:
                    res.append(word)
                elif len(res[-1])<=len(word):
                    res.pop()
                    res.append(word)

        res = sorted(res)
        return res[-1]

if __name__ == '__main__':
    # words = ["w","wo","wor","worl", "world"]
    words = ["a","banana","app","appl","ap","apply","apple"]
    result = Solution().longestWord(words)
    print(result)
