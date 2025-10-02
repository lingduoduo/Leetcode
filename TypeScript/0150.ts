class Solution {
  evalRPN(tokens: string[]): number {
    const stack: number[] = [];

    for (const t of tokens) {
      switch (t) {
        case '+': {
          const b = stack.pop()!;
          const a = stack.pop()!;
          stack.push(a + b);
          break;
        }
        case '-': {
          const b = stack.pop()!;
          const a = stack.pop()!;
          stack.push(a - b); // order matters
          break;
        }
        case '*': {
          const b = stack.pop()!;
          const a = stack.pop()!;
          stack.push(a * b);
          break;
        }
        case '/': {
          const b = stack.pop()!;
          const a = stack.pop()!;
          // truncate toward 0 as required by the LeetCode problem
          stack.push(Math.trunc(a / b));
          break;
        }
        default:
          stack.push(Number(t));
      }
    }
    return stack.pop()!;
  }
}
