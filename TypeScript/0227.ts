function calculate(s: string): number {
  const stack: number[] = [];
  let num = 0;
  let prevOp = "+"; // previous operator

  const isDigit = (ch: string) => ch >= "0" && ch <= "9";

  for (let i = 0; i < s.length; i++) {
    const ch = s[i];

    // Build current number
    if (isDigit(ch)) {
      num = num * 10 + (ch.charCodeAt(0) - "0".charCodeAt(0));
    }

    // If current char is an operator (or end of string), process previous op
    if ((!isDigit(ch) && ch !== " ") || i === s.length - 1) {
      if (prevOp === "+") {
        stack.push(num);
      } else if (prevOp === "-") {
        stack.push(-num);
      } else if (prevOp === "*") {
        const last = stack.pop()!;
        stack.push(last * num);
      } else if (prevOp === "/") {
        const last = stack.pop()!;
        // Truncate toward zero
        stack.push(last < 0 ? -Math.trunc(-last / num) : Math.trunc(last / num));
      }

      prevOp = ch;
      num = 0;
    }
  }

  return stack.reduce((a, b) => a + b, 0);
}
