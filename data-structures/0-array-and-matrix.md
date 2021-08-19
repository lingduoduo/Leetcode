### 数组与矩阵

1. 把数组中的 0 移到末尾

   283 - Move Zeroes (Easy)

```
For example, given nums = [0, 1, 0, 3, 12], after calling your function, nums should be [1, 3, 12, 0, 0].
public void moveZeroes(int[] nums) {
    int idx = 0;
    for (int num : nums) {
        if (num != 0) {
            nums[idx++] = num;
        }
    }
    while (idx < nums.length) {
        nums[idx++] = 0;
    }
}
```

```python
class Solution(object):
    def moveZeroes(self, nums):
        idx = 0
        for num in nums:
            if num != 0:
                nums[idx] = num 
                idx += 1
        while idx < len(nums):
            nums[idx] = 0 
            idx += 1


if __name__ == '__main__':
    res = Solution().moveZeroes(nums=[0, 1, 0, 3, 12])
    print(res)
```

2. 改变矩阵维度

   253 Reshape the Matrix (Easy)


```
Input:
nums =
[[1,2],
 [3,4]]
r = 1, c = 4

Output:
[[1,2,3,4]]

Explanation:
The row-traversing of nums is [1,2,3,4]. The new reshaped matrix is a 1 * 4 matrix, fill it row by row by using the previous list.
public int[][] matrixReshape(int[][] nums, int r, int c) {
    int m = nums.length, n = nums[0].length;
    if (m * n != r * c) {
        return nums;
    }
    int[][] reshapedNums = new int[r][c];
    int index = 0;
    for (int i = 0; i < r; i++) {
        for (int j = 0; j < c; j++) {
            reshapedNums[i][j] = nums[index / n][index % n];
            index++;
        }
    }
    return reshapedNums;
}
```

```python
class Solution(object):
    def matrixReshape(self, mat, r, c):
        m = len(mat)
        n = len(mat[0])
        if n == 0 and m == 0:
            return mat
        if n * m != r * c:
            return mat

        res = [[0] * c for _ in range(r)]
        idx = 0
        for i in range(r):
            for j in range(c):
                row, col = divmod(idx, n) 
                res[i][j] = mat[row][col]
                idx += 1
        return res   

if __name__ == '__main__':
    res = Solution().matrixReshape(mat = [[1,2],[3,4]], r = 1, c = 4)
    print(res)

    res = Solution().matrixReshape(mat = [[1,2],[3,4]], r = 4, c = 1)
    print(res)
```

3. 找出数组中最长的连续 1

485 Max Consecutive Ones (Easy)

```
public int findMaxConsecutiveOnes(int[] nums) {
    int max = 0, cur = 0;
    for (int x : nums) {
        cur = x == 0 ? 0 : cur + 1;
        max = Math.max(max, cur);
    }
    return max;
}
```

```python
class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        res = 0
        cur = 0
        for num in nums:
            if num == 1:
                cur += 1
                res = max(res, cur)
            else:
                cur = 0
        return res
```

4. 有序矩阵查找

240 Search a 2D Matrix II (Medium)

```
[
   [ 1,  5,  9],
   [10, 11, 13],
   [12, 13, 15]
]
public boolean searchMatrix(int[][] matrix, int target) {
    if (matrix == null || matrix.length == 0 || matrix[0].length == 0) return false;
    int m = matrix.length, n = matrix[0].length;
    int row = 0, col = n - 1;
    while (row < m && col >= 0) {
        if (target == matrix[row][col]) return true;
        else if (target < matrix[row][col]) col--;
        else row++;
    }
    return false;
}
```

```python
class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        if not matrix:
            return False
        
        r = 0
        c = len(matrix[0]) - 1
        while 0 <= r < len(matrix) and 0 <= c < len(matrix[0]):
            if matrix[r][c] == target:
                return True
            elif matrix[r][c] < target:
                r += 1
            else:
                c -= 1
        return False
```

5. 有序矩阵的 Kth Element

378 Kth Smallest Element in a Sorted Matrix ((Medium))

```
matrix = [
  [ 1,  5,  9],
  [10, 11, 13],
  [12, 13, 15]
],
k = 8,

return 13.
```

二分查找解法：

```
public int kthSmallest(int[][] matrix, int k) {
    int m = matrix.length, n = matrix[0].length;
    int lo = matrix[0][0], hi = matrix[m - 1][n - 1];
    while (lo <= hi) {
        int mid = lo + (hi - lo) / 2;
        int cnt = 0;
        for (int i = 0; i < m; i++) {
            for (int j = 0; j < n && matrix[i][j] <= mid; j++) {
                cnt++;
            }
        }
        if (cnt < k) lo = mid + 1;
        else hi = mid - 1;
    }
    return lo;
}
```

```python
from typing import List
class Solution:
    def kthSmallest(self, matrix: List[List[int]], k: int) -> int:
        m = len(matrix)
        n = len(matrix[0])
        l = matrix[0][0]
        r = matrix[m-1][n-1]

        while l <= r:
            mid = l + (r - l)//2
            cnt = 0
            for i in range(m):
                for j in range(n):
                    if matrix[i][j] <= mid:
                        cnt += 1
            if cnt < k:
                l = mid + 1
            else:
                r = mid - 1
        return l

if __name__ == '__main__':
    matrix = [[1, 5, 9], [10, 11, 13], [12, 13, 15]]
    k = 8
    result = Solution().kthSmallest(matrix, k)
    print(result)
```

堆解法：

```
public int kthSmallest(int[][] matrix, int k) {
    int m = matrix.length, n = matrix[0].length;
    PriorityQueue<Tuple> pq = new PriorityQueue<Tuple>();
    for(int j = 0; j < n; j++) pq.offer(new Tuple(0, j, matrix[0][j]));
    for(int i = 0; i < k - 1; i++) { // 小根堆，去掉 k - 1 个堆顶元素，此时堆顶元素就是第 k 的数
        Tuple t = pq.poll();
        if(t.x == m - 1) continue;
        pq.offer(new Tuple(t.x + 1, t.y, matrix[t.x + 1][t.y]));
    }
    return pq.poll().val;
}

class Tuple implements Comparable<Tuple> {
    int x, y, val;
    public Tuple(int x, int y, int val) {
        this.x = x; this.y = y; this.val = val;
    }

    @Override
    public int compareTo(Tuple that) {
        return this.val - that.val;
    }
}
```

```python
from typing import List
import heapq
class Solution:
    def kthSmallest(self, matrix: List[List[int]], k: int) -> int:
      nums = [matrix[i][j] for i in range(len(matrix)) for j in range(len(matrix[0]))]
        heapq.heapify(nums)
        for i in range(k):
            res = heapq.heappop(nums)
        return res
        
from typing import List
import heapq
import itertools
class Solution:
    def kthSmallest(self, matrix: List[List[int]], k: int) -> int:
        nums = list(itertools.chain(*matrix))
        heapq.heapify(nums)
        for i in range(k):
            res = heapq.heappop(nums)
        return res
```

6. 一个数组元素在 [1, n] 之间，其中一个数被替换为另一个数，找出重复的数和丢失的数

645 Set Mismatch (Easy)

```
Input: nums = [1,2,2,4]
Output: [2,3]
Input: nums = [1,2,2,4]
Output: [2,3]
```

最直接的方法是先对数组进行排序，这种方法时间复杂度为 O(NlogN)。本题可以以 O(N) 的时间复杂度、O(1) 空间复杂度来求解。

主要思想是通过交换数组元素，使得数组上的元素在正确的位置上。

```
public int[] findErrorNums(int[] nums) {
    for (int i = 0; i < nums.length; i++) {
        while (nums[i] != i + 1 && nums[nums[i] - 1] != nums[i]) {
            swap(nums, i, nums[i] - 1);
        }
    }
    for (int i = 0; i < nums.length; i++) {
        if (nums[i] != i + 1) {
            return new int[]{nums[i], i + 1};
        }
    }
    return null;
}

private void swap(int[] nums, int i, int j) {
    int tmp = nums[i];
    nums[i] = nums[j];
    nums[j] = tmp;
}
```

```python
class Solution:
    def findErrorNums(self, nums: List[int]) -> List[int]:
        for i in range(len(nums)):
            while nums[i] != i + 1:
                if nums[i] == nums[nums[i] - 1]:
                    break
                else:
                    j = nums[i] - 1
                    nums[i], nums[j] = nums[j], nums[i]
        res = []
        for i in range(len(nums)):
            if nums[i] != i + 1:
                res.extend([nums[i], i + 1])
        return res
```

7. 找出数组中重复的数，数组值在 [1, n] 之间

287 Find the Duplicate Number (Medium)

要求不能修改数组，也不能使用额外的空间。

```python
from typing import List
class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        for i in range(len(nums)):
            while nums[i] != i + 1:
                if nums[i] == nums[nums[i] - 1]:
                    return nums[i]
                else:
                    j = nums[i] - 1
                    nums[i], nums[j] = nums[j], nums[i]

if __name__ == '__main__':
    res = Solution().findDuplicate(nums = [1,3,4,2,2])
    print(res)
```

二分查找解法：

思路是我们在[1,N]范围内先求出mid，再统计小于等于mid的数字个数count，如果count<=mid，说明重复数字在[mid+1,N]中，否则在[1,mid)中。

我们统计小于等于mid的数字个数count，当nums在[1,mid]双闭区间中的数字不存在重复时，count应该恰好等于mid；当nums在[1,mid]双闭区间中的数字存在重复时，count应该>mid；当nums在[1,mid]双闭区间中的数字存在遗漏时，count应该<mid。所以，当我们发现count <= mid时，说明重复数字在[mid + 1, N]中，否则在[1,mid)中。

```
public int findDuplicate(int[] nums) {
     int l = 1, h = nums.length - 1;
     while (l <= h) {
         int mid = l + (h - l) / 2;
         int cnt = 0;
         for (int i = 0; i < nums.length; i++) {
             if (nums[i] <= mid) cnt++;
         }
         if (cnt > mid) h = mid - 1;
         else l = mid + 1;
     }
     return l;
}
```

```python
class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        n = len(nums)
        l = 0
        r = len(nums)
        while l <= r:
            mid = l + (r - l)//2
            cnt = 0
            for num in nums:
                if num <= mid:
                    cnt += 1
            if cnt <= mid:
                l = mid + 1
            else:
                r = mid - 1
        return l

if __name__ == '__main__':
    res = Solution().findDuplicate(nums = [1,3,4,2,2])
    print(res)
```

双指针解法，类似于有环链表中找出环的入口：

```
public int findDuplicate(int[] nums) {
    int slow = nums[0], fast = nums[nums[0]];
    while (slow != fast) {
        slow = nums[slow];
        fast = nums[nums[fast]];
    }
    fast = 0;
    while (slow != fast) {
        slow = nums[slow];
        fast = nums[fast];
    }
    return slow;
}
```
```python
class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        slow = nums[0]
        fast = nums[nums[0]]
        while slow != fast:
            fast = nums[nums[fast]]
            slow = nums[slow]
        fast = 0
        while slow != fast:
            fast = nums[fast]
            slow = nums[slow]
        return fast

if __name__ == '__main__':
    res = Solution().findDuplicate(nums = [1,3,4,2,2])
    print(res)
```

8. 数组相邻差值的个数

667 Beautiful Arrangement II (Medium)


```
Input: n = 3, k = 2
Output: [1, 3, 2]
Explanation: The [1, 3, 2] has three different positive integers ranging from 1 to 3, and the [2, 1] has exactly 2 distinct integers: 1 and 2.
```

题目描述：数组元素为 1~n 的整数，要求构建数组，使得相邻元素的差值不相同的个数为 k。

让前 k+1 个元素构建出 k 个不相同的差值，序列为：1 k+1 2 k 3 k-1 ... k/2 k/2+1.

```
public int[] constructArray(int n, int k) {
    int[] ret = new int[n];
    ret[0] = 1;
    for (int i = 1, interval = k; i <= k; i++, interval--) {
        ret[i] = i % 2 == 1 ? ret[i - 1] + interval : ret[i - 1] - interval;
    }
    for (int i = k + 1; i < n; i++) {
        ret[i] = i + 1;
    }
    return ret;
}
```
```python
from typing import List
class Solution:
    def constructArray(self, n: int, k: int) -> List[int]:
        res = [1]
        interval = k
        for i in range(1, k + 1):
            res.append(res[i - 1] + interval if i % 2 == 1 else res[i - 1] - interval)
            interval -= 1
            print(res)
        for i in range(k + 1, n):
            res.append(i + 1)
        return res
      
if __name__ == '__main__':
    res = Solution().constructArray(n = 3, k = 2)
    print(res)

    res = Solution().constructArray(n = 5, k = 2)
    print(res)
```

9. 数组的度
697 Degree of an Array (Easy)

```
Input: [1,2,2,3,1,4,2]
Output: 6
```

题目描述：数组的度定义为元素出现的最高频率，例如上面的数组度为 3。要求找到一个最小的子数组，这个子数组的度和原数组一样。

```
public int findShortestSubArray(int[] nums) {
    Map<Integer, Integer> numsCnt = new HashMap<>();
    Map<Integer, Integer> numsLastIndex = new HashMap<>();
    Map<Integer, Integer> numsFirstIndex = new HashMap<>();
    for (int i = 0; i < nums.length; i++) {
        int num = nums[i];
        numsCnt.put(num, numsCnt.getOrDefault(num, 0) + 1);
        numsLastIndex.put(num, i);
        if (!numsFirstIndex.containsKey(num)) {
            numsFirstIndex.put(num, i);
        }
    }
    int maxCnt = 0;
    for (int num : nums) {
        maxCnt = Math.max(maxCnt, numsCnt.get(num));
    }
    int ret = nums.length;
    for (int i = 0; i < nums.length; i++) {
        int num = nums[i];
        int cnt = numsCnt.get(num);
        if (cnt != maxCnt) continue;
        ret = Math.min(ret, numsLastIndex.get(num) - numsFirstIndex.get(num) + 1);
    }
    return ret;
}
```
```python

```
