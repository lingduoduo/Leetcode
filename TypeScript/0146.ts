class LRUCache {
  private d: Map<number, number>;
  private count: number; // capacity

  constructor(capacity: number) {
    this.d = new Map<number, number>();
    this.count = capacity;
  }

  get(key: number): number {
    if (!this.d.has(key)) return -1;
    const val = this.d.get(key)!;
    // move to most-recent: delete then re-set
    this.d.delete(key);
    this.d.set(key, val);
    return val;
    }

  put(key: number, value: number): void {
    if (this.d.has(key)) {
      // update & move to most-recent
      this.d.delete(key);
      this.d.set(key, value);
      return;
    }

    // evict least-recent if at capacity
    if (this.d.size >= this.count) {
      const oldestKey = this.d.keys().next().value;
      this.d.delete(oldestKey);
    }
    this.d.set(key, value);
  }
}

/**
 * Your LRUCache object will be instantiated and called as such:
 * var obj = new LRUCache(capacity)
 * var param_1 = obj.get(key)
 * obj.put(key,value)
 */
