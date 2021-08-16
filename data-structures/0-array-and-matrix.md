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



 