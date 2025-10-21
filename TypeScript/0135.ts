function candy(ratings: number[]): number {
  const n = ratings.length;
  const res: number[] = [1];

  // left → right
  for (let i = 1; i < n; i++) {
    if (ratings[i] > ratings[i - 1]) {
      res.push(res[i - 1] + 1);   // use i-1, not n-1
    } else {
      res.push(1);                // need a 1 when not increasing
    }
  }

  // right → left
  for (let i = n - 2; i >= 0; i--) {
    if (ratings[i] > ratings[i + 1]) {
      res[i] = Math.max(res[i], res[i + 1] + 1);
    }
  }

  // sum (Math.sum doesn't exist)
  return res.reduce((a, b) => a + b, 0);
}