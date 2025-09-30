class Solution {
  commonChars(words: string[]): string[] {
    if (!words || words.length === 0) return [];

    const base = 'a'.charCodeAt(0);
    const freq: number[] = Array(26).fill(0);
    for (const ch of words[0]) {
      freq[ch.charCodeAt(0) - base]++;
    }
    for (let i = 1; i < words.length; i++) {
      const curr: number[] = Array(26).fill(0);
      for (const ch of words[i]) {
        curr[ch.charCodeAt(0) - base]++;
      }
      for (let k = 0; k < 26; k++) {
        freq[k] = Math.min(freq[k], curr[k]);
      }
    }
    const res: string[] = [];
    for (let k = 0; k < 26; k++) {
      for (let cnt = 0; cnt < freq[k]; cnt++) {
        res.push(String.fromCharCode(base + k));
      }
    }
    return res;
  }
}

// Example:
const sol = new Solution();
console.log(sol.commonChars(["bella", "label", "roller"])); // ['e', 'l', 'l']
