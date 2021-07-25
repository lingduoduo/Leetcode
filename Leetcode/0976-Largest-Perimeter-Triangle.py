class Solution:
	 def largestPerimeter(self, nums: List[int]) -> int:
'''
if A[i] >= A[i+1] + A[i+2], then A[i] >= A[i+j] + A[i+k], 1 < j < k
if A[i] < A[i+1] + A[i+2], then A[i] + A[i+1] + A[i+2] is the answer

class Solution {
public:
  int largestPerimeter(vector<int>& A) {
    sort(rbegin(A), rend(A));
    for (int i = 0; i < A.size() - 2; ++i)
      if (A[i] < A[i + 1] + A[i + 2])
        return A[i] + A[i + 1] + A[i + 2];
    return 0;
  }
};
        A.sort()
        N = len(A)
        res = 0
        # A[i - 2], A[i - 1], A[i]
        for i in range(N - 1, 1, -1):
            if A[i - 2] + A[i - 1] > A[i]:
                return A[i - 2] + A[i - 1] + A[i]
        return 0

'''
        nums.sort()
        N = len(nums)
        for i in range(N-2):
            if nums[N-1-i] < nums[N-1-i-1] + nums[N-1-i-2]:
                return nums[N-1-i] + nums[N-1-i-1] + nums[N-1-i-2]
        return 0
        

