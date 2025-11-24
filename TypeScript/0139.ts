function wordBreak(s: string, wordDict: string[]): boolean {
    const n = s.length;
    const dp: boolean[] = new Array(n + 1).fill(false);
    dp[0] = true;
    for (let i = 1; i <= n; i++) {
        for (const w of wordDict) {
            const l = w.length;
            if (s.slice(i - l, i) === w && dp[i - l]) {
                dp[i] = true;
                break;
            }
        }
    }
    return dp[n];    
};