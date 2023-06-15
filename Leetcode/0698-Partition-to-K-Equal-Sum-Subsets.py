class Solution:
    """
    1) 首先计算数组中所有元素和sum，如果sum不能被k整除，则结果为false，否则计算划分后每组的和 subSum = sum/k;

    2) 对数组进行非降序排序，从后往前遍历，如果最大的元素比subSum大，说明存在元素没法划分，结果为false，否则将所有等于sunSum的元素挑出来单独为一组，分成i组，此时剩下j个元素;

    3) 将剩下的j个元素(0,1,2..j-1)分成k-i组，可以使用回溯法不断的去尝试，对于元素j-1,如果可以放入第一组且剩下j-1个元素可以放入k-i组中，则存在这样的划分，否则，将元素j-1从第一组拿出来尝试放入第二组，知道所有的元素尝试完;

    4) 如果元素尝试完都没有找到可能的划分，则不存在这样的划分.
    """

    def canPartitionKSubsets(self, nums: List[int], k: int) -> bool:
        psum = sum(nums) // k
        if sum(nums) % k != 0 or max(nums) > psum:
            return False

        nums.sort(reverse=True)
        target = [psum] * k

        def dfs(index, target):
            if index == len(nums):
                return True
            for i in range(k):
                if target[i] >= nums[index]:
                    target[i] -= nums[index]
                    if dfs(index + 1, target):
                        return True
                    target[i] += nums[index]
            return False

        return dfs(0, target)
