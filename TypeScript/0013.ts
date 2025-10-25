function romanToInt(s: string): number {
  const values: Record<string, number> = {
      I: 1,
      V: 5,
      X: 10,
      L: 50,
      C: 100,
      D: 500,
      M: 1000,
      IV: 4,
      IX: 9,
      XL: 40,
      XC: 90,
      CD: 400,
      CM: 900,
  };

  let res = 0;
  let i = 0;

  while (i < s.length) {
    // Check 2-character combination first, e.g., "IV", "CM"
    if (i < s.length - 1 && values[s.substring(i, i + 2)] !== undefined) {
      res += values[s.substring(i, i + 2)];
      i += 2;
    } else {
      // Otherwise, add single Roman numeral
      res += values[s[i]];
      i += 1;
    }
  }
  return res;
}