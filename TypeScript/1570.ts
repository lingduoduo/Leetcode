class SparseVector {
  private d: Map<number, number>;

  constructor(nums: number[]) {
    this.d = new Map();
    for (let i = 0; i < nums.length; i++) {
      const v = nums[i];
      if (v !== 0) {
        this.d.set(i, v);
      }
    }
  }

  dotProduct(vec: SparseVector): number {
    let res = 0;
    const [smaller, larger] =
      this.d.size < vec.d.size ? [this.d, vec.d] : [vec.d, this.d];

    for (const [k, v] of smaller.entries()) {
      if (larger.has(k)) {
        res += v * (larger.get(k) || 0);
      }
    }
    return res;
  }
}
