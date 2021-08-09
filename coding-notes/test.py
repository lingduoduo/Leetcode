class Solution:
    def inversePairs(self, nums):
        self.res = [0] * len(nums)
        return self.mergeSort(nums, 0, len(nums)-1)

    def mergeSort(self, A, l, r):
        if l >= r:
            return 0
        
        m = (l + r) >> 1
        ans = self.mergeSort(A, l, m) + self.mergeSort(A, m + 1, r)

        i, j, k = l, m + 1, l
        while i <= m and j <= r:
            if A[i] > A[j]:
                self.res[k] = A[j]
                j += 1
                ans += m - i + 1
            else:
                self.res[k] = A[i]
                i += 1
            k += 1
    
        while i <= m:
            self.res[k] = A[i]
            k += 1
            i += 1
        while j <= r:
            self.res[k] = A[j]
            k += 1
            j += 1
        for i in range(l, r + 1):
            A[i] = self.res[i]
        print(A)

        return ans

if __name__ == '__main__':
    res = Solution().inversePairs(nums=[2, 4, 1, 3, 5])
    print(res)


