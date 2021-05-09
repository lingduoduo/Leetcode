import collections
class Solution:
    def balancedString(self, s: str) -> int:
        n = len(s)
        cnt, avg = [None] * (n + 1), n//4
        cnt[0] = {'Q':0, 'W':0, 'E':0, 'R':0}
        for i, v in enumerate(s):
            cnt[i+1] = {k:v for k, v in cnt[i].items()}
            cnt[i+1][v] += 1
        
        def check(x):
            for st in range(n - x + 1):
                t = {k:cnt[n][k] - cnt[st+x][k] + cnt[st][k] for k in cnt[0].keys()}
                if all(avg >= t[x] for x in 'QWER'):
                    return True
            return False
            
        l, r = 0, n
        while l < r:
            mid = l + r >> 1
            if check(mid):
                r = mid
            else:
                l = mid + 1   
        return l

if __name__ == '__main__':
	# s = "QWER"
	# res = Solution().balancedString(s)
	# print(res)

	s = "WWEQERQWQWWRWWERQWEQ"
	res = Solution().balancedString(s)
	print(res)