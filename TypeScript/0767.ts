function reorganizeString(s: string): string {
  // freq map
  const d = new Map<string, number>();
  for (let i = 0; i < s.length; i++) {
    const ch = s[i];
    d.set(ch, (d.get(ch) ?? 0) + 1);
  }

  // Max-heap implementation for [freq, char]
  type Node = [number, string];
  class MaxHeap {
    private a: Node[] = [];
    size() { return this.a.length; }
    push(x: Node) {
      this.a.push(x);
      this.up(this.a.length - 1);
    }
    pop(): Node | undefined {
      if (!this.a.length) return undefined;
      const top = this.a[0];
      const last = this.a.pop()!;
      if (this.a.length) {
        this.a[0] = last;
        this.down(0);
      }
      return top;
    }
    private up(i: number) {
      while (i > 0) {
        const p = (i - 1) >> 1;
        if (this.a[p][0] >= this.a[i][0]) break;
        [this.a[p], this.a[i]] = [this.a[i], this.a[p]];
        i = p;
      }
    }
    private down(i: number) {
      const n = this.a.length;
      while (true) {
        let l = i * 2 + 1, r = l + 1, m = i;
        if (l < n && this.a[l][0] > this.a[m][0]) m = l;
        if (r < n && this.a[r][0] > this.a[m][0]) m = r;
        if (m === i) break;
        [this.a[m], this.a[i]] = [this.a[i], this.a[m]];
        i = m;
      }
    }
  }

  const maxHeap = new MaxHeap();
  for (const [ch, cnt] of d) {
    maxHeap.push([cnt, ch]);
  }

  const res: string[] = [];
  while (maxHeap.size() >= 2) {
    let [f1, c1] = maxHeap.pop()!;
    let [f2, c2] = maxHeap.pop()!;
    res.push(c1, c2);
    if (--f1 > 0) maxHeap.push([f1, c1]);
    if (--f2 > 0) maxHeap.push([f2, c2]);
  }

  if (maxHeap.size() === 1) {
    const [f, c] = maxHeap.pop()!;
    if (f > 1) return ""; // impossible to place without adjacency
    res.push(c);
  }

  return res.join("");
}
