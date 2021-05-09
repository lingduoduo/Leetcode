# class Solution:
#     def lexicalOrder(self, n: int) -> List[int]:
#         chas = sorted([str(i) for i in range(1, n+1)])
#         return [int(cha) for cha in chas]

class Solution:
    def lexicalOrder(self, n: int):
        cur = 1
        res = []
        for i in range(n):
            res.append(cur)
            if cur * 10 <= n:
                cur *= 10
            else:
                if cur >= n:
                    cur //= 10
                cur += 1
                while cur % 10 == 0:
                    cur //= 10
        return res

if __name__ == '__main__':
	res = Solution().lexicalOrder(100)
	print(res)        