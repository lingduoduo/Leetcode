class Solution:
    def countPartitions(self, nums: List[int], k: int) -> int:
        MOD = 10**9 + 7
        n = len(nums)

        # dp[i] = ways to partition nums[0:i]
        dp = [0] * (n + 1)
        pref = [0] * (n + 1)  # pref[i] = dp[0] + ... + dp[i] (mod)

        dp[0] = 1
        pref[0] = 1

        maxdq = deque()  # indices, nums decreasing -> front is max
        mindq = deque()  # indices, nums increasing -> front is min
        l = 0

        for i in range(1, n + 1):
            r = i - 1

            # push nums[r] into maxdq
            while maxdq and nums[maxdq[-1]] <= nums[r]:
                maxdq.pop()
            maxdq.append(r)

            # push nums[r] into mindq
            while mindq and nums[mindq[-1]] >= nums[r]:
                mindq.pop()
            mindq.append(r)

            # shrink window until valid
            while nums[maxdq[0]] - nums[mindq[0]] > k:
                l += 1
                if maxdq[0] < l:
                    maxdq.popleft()
                if mindq[0] < l:
                    mindq.popleft()

            # dp[i] = sum_{j=l..r} dp[j]
            # = pref[r] - pref[l-1]
            total = pref[r]
            if l > 0:
                total = (total - pref[l - 1]) % MOD

            dp[i] = total
            pref[i] = (pref[i - 1] + dp[i]) % MOD

        return dp[n]
