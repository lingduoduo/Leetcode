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

