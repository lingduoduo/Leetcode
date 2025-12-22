class Solution:
    def wiggleSort(self, nums) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        # if not nums: return None

        nums.sort()
        mid = (len(nums) - 1) // 2

        left = nums[mid::-1]
        right = nums[:mid:-1]

        for i in range(len(nums)):
            if i % 2 == 0 and left:
                nums[i] = left.pop(0)
            elif i % 2 == 1 and right:
                nums[i] = right.pop(0)
        return nums

class Solution:
    def wiggleSort(self, nums: List[int]) -> None:
        n = len(nums)
        if n <= 1:
            return

        # max-heap via negatives
        maxh = [-x for x in nums]
        heapq.heapify(maxh)

        # Fill odd indices first (1,3,5,...) with the largest values,
        # then fill even indices (0,2,4,...) with the remaining.
        idx_order = list(range(1, n, 2)) + list(range(0, n, 2))
        print(idx_order)

        for idx in idx_order:
            nums[idx] = -heapq.heappop(maxh)
        return nums

if __name__ == "__main__":
    # nums = [5,1,1,6,2]
    nums = [1, 3, 2, 2, 3, 1]
    results = Solution().wiggleSort(nums)
    print(results)
