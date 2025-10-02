class Solution {
  decodeString(s: string): string {
    const stack: Array<[string, number]> = [];
    let curr = '';
    let num = 0;

    for (let i = 0; i < s.length; i++) {
      const ch = s[i];

      if (ch >= '0' && ch <= '9') {
        num = num * 10 + (ch.charCodeAt(0) - 48); // build multi-digit numbers
      } else if (ch === '[') {
        stack.push([curr, num]); // save state
        curr = '';
        num = 0;
      } else if (ch === ']') {
        const [prev, k] = stack.pop()!;
        curr = prev + curr.repeat(k); // expand
      } else {
        curr += ch; // regular letter
      }
    }
    return curr;
  }
}

// quick checks
const sol = new Solution();
console.log(sol.decodeString("3[a]2[bc]"));        // "aaabcbc"
console.log(sol.decodeString("3[a2[c]]"));         // "accaccacc"
console.log(sol.decodeString("2[abc]3[cd]ef"));    // "abcabccdcdcdef"
console.log(sol.decodeString("10[a]"));            // "aaaaaaaaaa"
