class MyCircularDeque {
  private arr: number[];
  private cap: number;
  private head: number; // index of current front
  private tail: number; // index one past current rear
  private size: number;

  constructor(k: number) {
    this.arr = new Array(k);
    this.cap = k;
    this.head = 0;
    this.tail = 0;
    this.size = 0;
  }

  insertFront(value: number): boolean {
    if (this.isFull()) return false;
    this.head = (this.head - 1 + this.cap) % this.cap;
    this.arr[this.head] = value;
    this.size++;
    return true;
  }

  insertLast(value: number): boolean {
    if (this.isFull()) return false;
    this.arr[this.tail] = value;
    this.tail = (this.tail + 1) % this.cap;
    this.size++;
    return true;
  }

  deleteFront(): boolean {
    if (this.isEmpty()) return false;
    this.head = (this.head + 1) % this.cap;
    this.size--;
    return true;
  }

  deleteLast(): boolean {
    if (this.isEmpty()) return false;
    this.tail = (this.tail - 1 + this.cap) % this.cap;
    this.size--;
    return true;
  }

  getFront(): number {
    if (this.isEmpty()) return -1;
    return this.arr[this.head];
  }

  getRear(): number {
    if (this.isEmpty()) return -1;
    const idx = (this.tail - 1 + this.cap) % this.cap;
    return this.arr[idx];
  }

  isEmpty(): boolean {
    return this.size === 0;
  }

  isFull(): boolean {
    return this.size === this.cap;
  }
}
