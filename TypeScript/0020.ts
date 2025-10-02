class Solution {
  isValid(s: string): boolean {
    const stack: string[] = [];

    for (const c of s) {
      if (c === '(') stack.push(')');
      else if (c === '[') stack.push(']');
      else if (c === '{') stack.push('}');
      else {
        // c is a closing bracket; must match the last expected closer
        if (stack.length === 0 || stack.pop() !== c) return false;
      }
    }
    return stack.length === 0;
  }
}

// ---- Tests ----
const sol = new Solution();
const tests: string[] = [
  "()",          // true
  "()[]{}",      // true
  "(]",          // false
  "([)]",        // false
  "{[]}",        // true
  "",            // true (empty string is valid)
  "(((((",       // false
  "(){}}{",      // false
  "[({})]",      // true
  "(((){[]}))",  // true
];

for (const t of tests) {
  console.log(`${t.padEnd(10)} -> ${sol.isValid(t)}`);
}
