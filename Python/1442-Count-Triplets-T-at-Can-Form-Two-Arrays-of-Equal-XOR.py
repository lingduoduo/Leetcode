class Solution:
    def countTriplets(self, arr) -> int:
        nums = [0] * (len(arr) + 1)
        for i in range(len(arr)):
            nums[i + 1] = nums[i] ^ arr[i]

        res = 0
        for i in range(len(arr) - 1):
            for j in range(i + 1, len(arr)):
                for k in range(j, len(arr)):
                    a = nums[i] ^ nums[j]
                    b = nums[j] ^ nums[k + 1]
                    if a == b:
                        res += 1
        return res


if __name__ == "__main__":
    arr = [2, 3, 1, 6, 7]
    results = Solution().countTriplets(arr)
    print(results)
