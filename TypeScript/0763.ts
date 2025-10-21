function partitionLabels(s: string): number[] {
  // map char -> [firstIndex, lastIndex]
  const d = new Map<string, [number, number]>();

  for (let i = 0; i < s.length; i++) {
    const ch = s[i];
    if (!d.has(ch)) d.set(ch, [i, i]);
    else d.get(ch)![1] = i;
  }

  // collect and sort ranges by start
  const nums = Array.from(d.values()).sort((a, b) => a[0] - b[0]);

  // merge overlapping ranges
  const merged: [number, number][] = [];
  for (const [x2, y2] of nums) {
    if (merged.length === 0 || merged[merged.length - 1][1] < x2) {
      merged.push([x2, y2]);
    } else {
      merged[merged.length - 1][1] = Math.max(merged[merged.length - 1][1], y2);
    }
  }

  // lengths of merged partitions
  return merged.map(([l, r]) => r - l + 1);
}