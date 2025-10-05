class MyStack {
  private queue_in: number[] = [];
  private queue_out: number[] = [];

  constructor() {}

  push(x: number): void {
    this.queue_in.push(x);
  }

  pop(): number {
    if (this.empty()) throw new Error("Stack is empty");
    // Move all but last from queue_in -> queue_out
    while (this.queue_in.length > 1) {
      this.queue_out.push(this.queue_in.shift()!);
    }
    const res = this.queue_in.shift()!; // last is the stack top
    // swap queues
    [this.queue_in, this.queue_out] = [this.queue_out, this.queue_in];
    return res;
  }

  top(): number {
    if (this.empty()) throw new Error("Stack is empty");
    while (this.queue_in.length > 1) {
      this.queue_out.push(this.queue_in.shift()!);
    }
    const res = this.queue_in.shift()!; // peek top
    this.queue_out.push(res);           // put it back
    [this.queue_in, this.queue_out] = [this.queue_out, this.queue_in];
    return res;
  }

  empty(): boolean {
    return this.queue_in.length === 0 && this.queue_out.length === 0;
  }
}

/**
 * Your MyStack object will be instantiated and called as such:
 * var obj = new MyStack()
 * obj.push(x)
 * var param_2 = obj.pop()
 * var param_3 = obj.top()
 * var param_4 = obj.empty()
 */