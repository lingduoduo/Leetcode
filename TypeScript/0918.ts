type Entry = [timestamp: number, value: string];

class TimeMap {
  private dic: Map<string, Entry[]>;

  constructor() {
    this.dic = new Map();
  }

  // O(1) amortized (timestamps assumed non-decreasing for each key)
  set(key: string, value: string, timestamp: number): void {
    const arr = this.dic.get(key) ?? [];
    arr.push([timestamp, value]);
    this.dic.set(key, arr);
  }

  // O(log n) — returns value with the greatest timestamp <= given timestamp
  get(key: string, timestamp: number): string {
    const arr = this.dic.get(key);
    if (!arr || arr.length === 0) return "";

    let left = 0;
    let right = arr.length; // exclusive upper bound

    while (left < right) {
      const mid = Math.floor((left + right) / 2);
      if (arr[mid][0] <= timestamp) {
        left = mid + 1;
      } else {
        right = mid;
      }
    }

    return right === 0 ? "" : arr[right - 1][1];
  }

  /**
   * Delete the entry for `key` at the exact `timestamp`.
   * Returns true if an entry was removed, false if none matched.
   * O(log n)
   */
  delete(key: string, timestamp: number): boolean {
    const arr = this.dic.get(key);
    if (!arr) return false;

    let left = 0;
    let right = arr.length - 1;

    while (left <= right) {
      const mid = Math.floor((left + right) / 2);
      const t = arr[mid][0];
      if (t === timestamp) {
        arr.splice(mid, 1);
        if (arr.length === 0) this.dic.delete(key);
        else this.dic.set(key, arr);
        return true;
      } else if (t < timestamp) {
        left = mid + 1;
      } else {
        right = mid - 1;
      }
    }

    return false;
  }

  // (Optional) remove all timestamps for a key
  // deleteKey(key: string): boolean {
  //   return this.dic.delete(key);
  // }
}
