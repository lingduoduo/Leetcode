class Solution:
    def addBoldTag(self, s: str, words: List[str]) -> str:
        n = len(s)
        bold = [False] * n

        # Mark bold intervals
        for word in words:
            start = s.find(word)
            while start != -1:
                end = start + len(word)
                for i in range(start, end):
                    bold[i] = True
                start = s.find(word, start + 1)

        # Build result with <b> and </b>
        res = []
        i = 0
        while i < n:
            if bold[i]:
                res.append("<b>")
                while i < n and bold[i]:
                    res.append(s[i])
                    i += 1
                res.append("</b>")
            else:
                res.append(s[i])
                i += 1

        return "".join(res)