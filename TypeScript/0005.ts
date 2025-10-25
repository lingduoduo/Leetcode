function longestPalindrome(s: string): string {
  const n = s.length;
  if (n === 0) return "";

  // dp[i][j] = s[i..j] is a palindrome
  const dp: boolean[][] = Array.from({ length: n }, () => Array(n).fill(false));

  let max_len = 1;
  let start = 0;
  let end = 0;

  // Fill by increasing substring length (i from n-1 down to 0 works too)
  for (let i = n - 1; i >= 0; i--) {
    for (let j = i; j < n; j++) {
      if (s[i] === s[j]) {
        // length < 3 covers 1-char and 2-char substrings
        if (j - i < 3 || dp[i + 1][j - 1]) {
          dp[i][j] = true;
          if (j - i + 1 > max_len) {
            max_len = j - i + 1;
            start = i;
            end = j;
          }
        }
      }
    }
  }

  return s.slice(start, end + 1);
}
