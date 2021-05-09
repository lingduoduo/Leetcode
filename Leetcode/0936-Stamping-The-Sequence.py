class Solution:
    def movesToStamp(self, stamp: str, target: str) -> List[int]:
        def check(word):
            ret = 0
            for i in range(m):
                if word[i] == '?':
                    continue
                if word[i] == stamp[i]:
                    ret += 1
                else:
                    return 0
            return ret

        target = list(target)
        m, n = len(stamp), len(target)
        tot, res = 0, []
        while tot < n:
            tmp = tot
            for i in range(n - m + 1):
                cur = check(target[i : i + m])
                if cur:
                    tot += cur
                    target[i : i + m] = ['?'] * m
                    res.append(i)
            if tmp == tot:
                return []
        return res [::-1]

