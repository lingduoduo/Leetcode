class Solution {
  isHappy(n: number): boolean {
    const seen = new Set<number>();
    const getSum = (num: number): number => {
      let tot = 0;
      while (num > 0) {
        const d = num % 10;
        tot += d * d;                 // sum of squares of digits
        num = Math.floor(num / 10);
      }
      return tot;
    };

    while (n !== 1 && !seen.has(n)) {
      seen.add(n);
      n = getSum(n);
    }
    return n === 1;
  }
}

// Example
const sol = new Solution();
console.log(sol.isHappy(19)); // true
console.log(sol.isHappy(2));  // false
