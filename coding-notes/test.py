import collections
class Solution(object):
    def maxInWindows(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """
        que = collections.deque() # [[i, num]]
        res = []
        for i, num in enumerate(nums):
            if que and i - que[0][0] >= k:
                que.popleft()
            while que and que[-1][1] <= num:
                que.pop()
            que.append([i, num])
            if i >= k - 1:
                res.append(que[0][1])
        return res


import heapq
class Solution:
    def maxInWindows(self, nums, k):
        if len(nums) < k or k < 1:
            return nums

        res = []
        heap = []
        for i in range(k):
            heap.append(nums[i])
        res.append(heapq.nlargest(1, heap)[0])

        for i in range(k, len(nums)):
            heap.pop(0)
            heap.append(nums[i])
            res.append(heapq.nlargest(1, heap)[0])
        return res

if __name__ == '__main__':
    res = Solution().maxInWindows(nums=[2, 3, 4, 2, 6, 2, 5, 1], k = 3)
    print(res)


# # ```java
# public ArrayList<Integer> maxInWindows(int[] num, int size) {
#     ArrayList<Integer> ret = new ArrayList<>();
#     if (size > num.length || size < 1)
#         return ret;
#     PriorityQueue<Integer> heap = new PriorityQueue<>((o1, o2) -> o2 - o1);  /* 大顶堆 */
#     for (int i = 0; i < size; i++)
#         heap.add(num[i]);
#     ret.add(heap.peek());
#     for (int i = 0, j = i + size; j < num.length; i++, j++) {            /* 维护一个大小为 size 的大顶堆 */
#         heap.remove(num[i]);
#         heap.add(num[j]);
#         ret.add(heap.peek());
#     }
#     return ret;
# # ```