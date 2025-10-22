function monotoneIncreasingDigits(n: number): number {
  if (n === 0) return 0;

  // Keep your digit extraction idea
  const digits: number[] = [];
  while (n > 0) {
    digits.push(n % 10);
    n = Math.floor(n / 10);
  }

  // Work in most-significant-first order
  digits.reverse();

  // Walk from right to left; when a drop is found, decrement left and mark tail
  let mark = digits.length;
  for (let i = digits.length - 1; i > 0; i--) {
    if (digits[i - 1] > digits[i]) {
      digits[i - 1]--;
      mark = i; // everything from here becomes 9
    }
  }

  for (let i = mark; i < digits.length; i++) digits[i] = 9;

  // Rebuild the number
  let res = 0;
  for (const d of digits) res = res * 10 + d;
  return res;
}
