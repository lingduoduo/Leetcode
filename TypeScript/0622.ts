class MyCircularQueue {
    private cap;
    private q = [];
    private ct = 0;
    private head = 0;
    constructor(k: number) {
        this.cap = k;
        this.q = [];
        this.ct = 0;
        this.head = 0;
    }

    enQueue(value: number): boolean {
        if (this.isFull()) return false;
        this.q[(this.head + this.ct) % this.cap] = value;
        this.ct += 1;
        return true
    }

    deQueue(): boolean {
        if (this.isEmpty()) return false;
        this.head = (this.head + 1) % this.cap;
        this.ct -= 1
        return true;
    }

    Front(): number {
        if (!this.ct)
            return -1
        return this.q[this.head];
    }

    Rear(): number {
        if (!this.ct)
            return -1
        return this.q[(this.head + this.ct - 1) % this.cap];
    }

    isEmpty(): boolean {
        return this.ct === 0
    }

    isFull(): boolean {
        return this.ct == this.cap;
    }
}






/**
 * Your MyCircularQueue object will be instantiated and called as such:
 * var obj = new MyCircularQueue(k)
 * var param_1 = obj.enQueue(value)
 * var param_2 = obj.deQueue()
 * var param_3 = obj.Front()
 * var param_4 = obj.Rear()
 * var param_5 = obj.isEmpty()
 * var param_6 = obj.isFull()
 */


