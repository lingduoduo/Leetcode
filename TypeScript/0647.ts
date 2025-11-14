function countSubstrings(s: string): number {
    let n = s.length;
    let dp: boolean[][] = Array.from({ length: n }, () => Array(n).fill(false));
    let res = 0;

    for (let end = 0; end < n; end++) {                 // end index
        for (let start = 0; start <= end; start++) {     // start index (0..end)
            if (s[start] === s[end] && (end - start <= 1 || dp[start + 1][end - 1])) {
                dp[start][end] = true;
                res++;
            }
        }
    }
    return res;
};
