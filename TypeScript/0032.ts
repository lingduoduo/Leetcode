function longestValidParentheses(s: string): number {
  let stack: number[] = [-1]; // sentinel
  let res = 0;

  for (let i = 0; i < s.length; i++) {
    if (s[i] === "(") {
      stack.push(i);
    } else {
      stack.pop(); // match a '(' if possible
      if (stack.length === 0) {
        // no base -> set new base at current ')'
        stack.push(i);
      } else {
        res = Math.max(res, i - stack[stack.length - 1]);
      }
    }
  }
  return res;
}