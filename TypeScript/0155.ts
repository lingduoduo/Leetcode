class MinStack {
  private stack: number[] = [];
  private minStack: number[] = [];

  constructor() {}

  push(val: number): void {
    this.stack.push(val);
    if (this.minStack.length === 0) {
      this.minStack.push(val);
    } else {
      const currMin = this.minStack[this.minStack.length - 1];
      this.minStack.push(Math.min(currMin, val));
    }
  }

  pop(): void {
    // LeetCode signature returns void
    this.stack.pop();
    this.minStack.pop();
  }

  top(): number {
    return this.stack[this.stack.length - 1];
  }

  getMin(): number {
    return this.minStack[this.minStack.length - 1];
  }
}
