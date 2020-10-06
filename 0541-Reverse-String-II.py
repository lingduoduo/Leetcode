class Solution:
    def reverseStr(self, s: str, k: int) -> str:
        if len(s)<k:
            return s[::-1]
        elif len(s)<2*k:
            tmp = s[0:k]
            return tmp[::-1] + s[k:]
        else:
            res = ''
            step = len(s)//k
            for i in range(step):
                tmp = s[i*k : (i+1)*k]
                if i%2 ==0:
                    res += tmp[::-1]
                else:
                    res += tmp
            if step % 2 == 1:
                res += s[step*k:]
            else:
                tmp = s[step*k:]
                res += tmp[::-1]
            return res

if __name__ == '__main__':
    s = "abcdefg"
    k = 2
    result = Solution().reverseStr(s, k)
    print(result)