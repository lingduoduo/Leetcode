function lemonadeChange(bills: number[]): boolean {
  const d = new Map<number, number>([
    [5, 0],
    [10, 0],
  ]);

  for (const bill of bills) {
    if (bill === 5) {
      d.set(5, (d.get(5) ?? 0) + 1);
    } else if (bill === 10) {
      if ((d.get(5) ?? 0) === 0) return false;
      d.set(5, (d.get(5) ?? 0) - 1);
      d.set(10, (d.get(10) ?? 0) + 1);
    } else if (bill === 20) {
      if ((d.get(10) ?? 0) > 0 && (d.get(5) ?? 0) > 0) {
        d.set(10, (d.get(10) ?? 0) - 1);
        d.set(5, (d.get(5) ?? 0) - 1);
      } else if ((d.get(5) ?? 0) >= 3) {
        d.set(5, (d.get(5) ?? 0) - 3);
      } else {
        return false;
      }
    }
  }
  return true;
}