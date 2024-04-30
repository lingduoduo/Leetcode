from typing import List


class Solution:
    def countSmaller(self, nums: List[int]) -> List[int]:
        # implement segment tree
        def update(index, value, tree, size):
            index += size  # shift the index to the leaf
            # update from leaf to root
            tree[index] += value
            while index > 1:
                index //= 2
                tree[index] = tree[index * 2] + tree[index * 2 + 1]

        def query(left, right, tree, size):
            # return sum of [left, right)
            result = 0
            left += size  # shift the index to the leaf
            right += size
            while left < right:
                # if left is a right node
                # bring the value and move to parent's right node
                if left % 2 == 1:
                    result += tree[left]
                    left += 1
                # else directly move to parent
                left //= 2
                # if right is a right node
                # bring the value of the left node and move to parent
                if right % 2 == 1:
                    right -= 1
                    result += tree[right]
                # else directly move to parent
                right //= 2
            return result

        offset = 10**4  # offset negative to non-negative
        size = 2 * 10**4 + 1  # total possible values in nums
        tree = [0] * (2 * size)
        result = []
        for num in reversed(nums):
            smaller_count = query(0, num + offset, tree, size)
            result.append(smaller_count)
            update(num + offset, 1, tree, size)
        return reversed(result)
    

class Solution:
    def countSmaller(self, nums: List[int]) -> List[int]:
        def countAndMergeSort(num_idxs, start, end, counts):
            if (
                end - start <= 0
            ):  # The size of range [start, end] less than 2 is always with count 0.
                return 0

            mid = start + (end - start) // 2
            countAndMergeSort(num_idxs, start, mid, counts)
            countAndMergeSort(num_idxs, mid + 1, end, counts)
            r = mid + 1
            tmp = []
            for i in range(start, mid + 1):
                # Merge the two sorted arrays into tmp.
                while r <= end and num_idxs[r][0] < num_idxs[i][0]:
                    tmp.append(num_idxs[r])
                    r += 1
                tmp.append(num_idxs[i])
                counts[num_idxs[i][1]] += r - (mid + 1)

            # Copy tmp back to num_idxs
            num_idxs[start : start + len(tmp)] = tmp

        num_idxs = []
        counts = [0] * len(nums)
        for i, num in enumerate(nums):
            num_idxs.append((num, i))
        countAndMergeSort(num_idxs, 0, len(num_idxs) - 1, counts)
        return counts
    

class Solution:
    def countSmaller(self, nums: List[int]) -> List[int]:
        # implement Binary Index Tree
        def update(index, value, tree, size):
            index += 1  # index in BIT is 1 more than the original index
            while index < size:
                tree[index] += value
                index += index & -index

        def query(index, tree):
            # return sum of [0, index)
            result = 0
            while index >= 1:
                result += tree[index]
                index -= index & -index
            return result

        offset = 10**4  # offset negative to non-negative
        size = 2 * 10**4 + 2  # total possible values in nums plus one dummy
        tree = [0] * size
        result = []
        for num in reversed(nums):
            smaller_count = query(num + offset, tree)
            result.append(smaller_count)
            update(num + offset, 1, tree, size)
        return reversed(result)