function calculate(s: string): number {
  let stack: Array<[number, number]> = []; // (sign, accumulatedResult)
  let cur = 0;
  let sign = 1;
  let res = 0;

  for (let i = 0; i < s.length; i++) {
    const ch = s[i];

    if (ch >= '0' && ch <= '9') {
      cur = cur * 10 + (ch.charCodeAt(0) - 48);
    } else if (ch === '+' || ch === '-') {
      res += sign * cur;
      sign = ch === '-' ? -1 : 1;
      cur = 0;
    } else if (ch === '(') {
      // push current context (sign, result)
      stack.push([sign, res]);
      // reset for new inner expression
      sign = 1;
      res = 0;
      cur = 0;
    } else if (ch === ')') {
      // finish inner expression
      res += sign * cur;
      const [prevSign, prevRes] = stack.pop()!;
      res = prevRes + prevSign * res;
      cur = 0;
    }
  }

  res += sign * cur;
  return res;
}
