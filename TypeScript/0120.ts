function minimumTotal(triangle: number[][]): number {
    let n = triangle.length;
    let dp: number[] = triangle[n - 1].slice();

    for (let i = n - 2; i >= 0; i--) {
        for (let j = 0; j < triangle[i].length; j++) {
            dp[j] = triangle[i][j] + Math.min(dp[j], dp[j + 1]);
        }
    }
    return dp[0];
};