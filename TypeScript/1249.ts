function minRemoveToMakeValid(s: string): string {
  let cnt = 0;
  let stack: string[] = [];

  // 1) Keep letters and valid parens; skip stray ')'
  for (let i = 0; i < s.length; i++) {
    const ch = s[i];
    if (ch === '(') {
      cnt++;
      stack.push(ch);
    } else if (ch === ')') {
      if (cnt > 0) {
        cnt--;
        stack.push(ch);
      } // else: skip invalid ')'
    } else {
      stack.push(ch); // keep letters/other chars
    }
  }

  // 2) Remove extra '(' from right to left
  for (let i = stack.length - 1; i >= 0 && cnt > 0; i--) {
    if (stack[i] === '(') {
      stack[i] = '';
      cnt--;
    }
  }

  return stack.join('');
}
