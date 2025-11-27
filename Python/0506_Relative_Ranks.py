class Solution:
    def findRelativeRanks(self, nums):
        d = {v: k for k, v in enumerate(nums)}
        nums.sort(reverse=True)

        rank = [1]
        res = [0] * len(nums)

        i = 0
        while i < len(nums):
            if rank[-1] == 1:
                res[d[nums[i]]] = "Gold Medal"
            elif rank[-1] == 2:
                res[d[nums[i]]] = "Silver Medal"
            elif rank[-1] == 3:
                res[d[nums[i]]] = "Bronze Medal"
            else:
                res[d[nums[i]]] = str((rank[-1]))
            rank.append(rank[-1] + 1)
            i += 1
        return res


if __name__ == "__main__":
    nums = [5, 4, 3, 2, 1]
    # nums = [10,3,8,9,4]
    results = Solution().findRelativeRanks(nums)
    print(results)
