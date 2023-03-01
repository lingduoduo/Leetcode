class Solution(object):
    def reverseWords(self, s):
        """
        :type s: str
        :rtype: str
        """
        ###s = s.strip()
        ###p = re.compile(r'\s{2,}')
        ###s = p.sub(" ", s)
        ###words = s.split(" ")
        ###return " ".join(words[::-1])
        
        if s == "":
            return s
        
        s = s.strip()
        ls = s.split(" ")
        if ls == []:
            return ""
        
        res = ""
        for i in range(len(ls)-1):
            if ls[len(ls)-1-i] != "":
                res += ls[len(ls)-1-i] + " "
        res += ls[0]
        
        return res


class Solution:
    def reverseWords(self, s: str) -> str:
        return " ".join(reversed(s.split()))


class Solution:
    def trim_spaces(self, s: str) -> list:
        left, right = 0, len(s) - 1
        # remove leading spaces
        while left <= right and s[left] == ' ':
            left += 1

        # remove trailing spaces
        while left <= right and s[right] == ' ':
            right -= 1

        # reduce multiple spaces to single one
        output = []
        while left <= right:
            if s[left] != ' ':
                output.append(s[left])
            elif output[-1] != ' ':
                output.append(s[left])
            left += 1

        return output

    def reverse(self, l: list, left: int, right: int) -> None:
        while left < right:
            l[left], l[right] = l[right], l[left]
            left, right = left + 1, right - 1

    def reverse_each_word(self, l: list) -> None:
        n = len(l)
        start = end = 0

        while start < n:
            # go to the end of the word
            while end < n and l[end] != ' ':
                end += 1
            # reverse the word
            self.reverse(l, start, end - 1)
            # move to the next word
            start = end + 1
            end += 1

    def reverseWords(self, s: str) -> str:
        # converst string to char array
        # and trim spaces at the same time
        l = self.trim_spaces(s)

        # reverse the whole string
        self.reverse(l, 0, len(l) - 1)

        # reverse each word
        self.reverse_each_word(l)

        return ''.join(l)


if __name__ == "__main__":
    s = "   the sky is blue   "
    result = Solution().reverseWords(s)
    print(result)