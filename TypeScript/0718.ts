function findLength(nums1: number[], nums2: number[]): number {
    let dp: number[][];
    dp = new Array(nums1.length).fill(0).map(() => new Array(nums2.length).fill(0) );
    let res: number = 0;
    for (let i = 0; i < nums1.length; i++) {
        for (let j = 0; j < nums2.length; j++) {
            if (nums1[i] === nums2[j]) {
                if (i === 0 || j === 0) {
                    dp[i][j] = 1;
                } else {
                    dp[i][j] = Math.max(dp[i][j], dp[i - 1][j - 1] + 1);
                }
            }
            res = Math.max(res, dp[i][j]);
        }
    }
    return res;
};

