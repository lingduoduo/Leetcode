function longestWPI(hours: number[]): number {
  const d = new Map<number, number>(); // prefix -> first index
  let presum = 0;
  let res = 0;

  for (let i = 0; i < hours.length; i++) {
    presum += hours[i] > 8 ? 1 : -1;

    if (presum > 0) {
      res = Math.max(res, i + 1); // whole prefix is well-performing
    } else {
      if (!d.has(presum)) d.set(presum, i); // store first time we see this prefix

      const prev = d.get(presum - 1);       // need a prefix smaller by 1
      if (prev !== undefined) {
        res = Math.max(res, i - prev);
      }
    }
  }
  return res;
}