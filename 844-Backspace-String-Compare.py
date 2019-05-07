class Solution(object):
    def backspaceCompare(self, S, T):
        """
        :type S: str
        :type T: str
        :rtype: bool
        """
        s = list()
        t = list()
        
        for i in range(len(S)):
            if S[i] != '#':
                s.append(S[i])
            else:
                if len(s) >= 1:
                    s.pop()
        
        for i in range(len(T)):
            if T[i] != '#':
                t.append(T[i])
            else:
                if len(t) >= 1:
                    t.pop()
        return s == t


if __name__ == '__main__':
    S = "ab#c"
    T = "ad#c"
    S = "ab##"
    T = "c#d#"
    S = "a##c"
    T = "#a#c"
    S = "a#c"
    T = "b"
    result = Solution().backspaceCompare(S, T)
    print(result)
