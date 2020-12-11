# class Solution:
#     def findMaximumXOR(self, nums: List[int]) -> int:
#         res = 0
#         for i in range(31, -1, -1):
#             res <<= 1
#             pre = set(n >> i for n in nums)
#             res += any(res ^ 1 ^ p in pre for p in pre)
#         return res


class Solution:
    def findMaximumXOR(self, nums) -> int:   
        res = mask = 0
        for x in reversed(range(32)):
            mask += 1 << x
            # print(bin(mask))
            prefixSet = set([n & mask for n in nums])
            # print(prefixSet)
            temp = res | 1 << x
            for prefix in prefixSet:
                if temp ^ prefix in prefixSet:
                    res = temp
                    break
        return res

if __name__ == '__main__':
	nums = [3,10,5,25,2,8]
	res = Solution().findMaximumXOR(nums)
	print(res)
