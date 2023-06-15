import collections
import re


class Solution(object):
    def checkRecord(self, s):
        """
        :type s: str
        :rtype: bool
        """
        ###a = 0
        ###l = 0
        ###for c in s:
        ###	if c == 'A':
        ###		a+=1
        ###	if c == 'L':
        ###		l+=1
        ###	else:
        ###		if l < 3:
        ###			l = 0
        ###if a>1 or l>2:
        ###	return False
        ###else:
        ###	return True

        ###i = 0
        ###a = 0
        ###while i < len(s):
        ###    if i < len(s) - 2 and s[i] == 'L' and s[i + 1] == 'L' and s[i + 2] == 'L':
        ###        return False
        ###    if s[i] == 'A':
        ###        a += 1
        ###    if a > 1:
        ###        return False
        ###    i += 1
        ###return True

        return not re.match(".*A.*A.*", s) and not re.match(".*LLL.*", s)

        d = collections.Counter(s)
        if d["A"] > 1:
            return False

        i = 0
        for i in range(len(s) - 2):
            ###print(s[i:(i+3)])
            if s[i : (i + 3)] == "LLL":
                return False
        return True


if __name__ == "__main__":
    s = "PPALLP"
    result = Solution().checkRecord(s)
    print(result)

    s = "LLLALL"
    result = Solution().checkRecord(s)
    print(result)

    s = "PPALLL"
    result = Solution().checkRecord(s)
    print(result)

    s = "LLPPPLL"
    result = Solution().checkRecord(s)
    print(result)
