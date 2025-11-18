import { Heap } from "heap-js";

// No imports here – LeetCode provides `Heap` globally.

class MedianFinder {
    private small: Heap<number>; // max-heap (lower half)
    private large: Heap<number>; // min-heap (upper half)

    constructor() {
        // Max-heap: larger number should come first -> descending
        this.small = new Heap<number>((a, b) => b - a);
        // Min-heap: smaller number should come first -> ascending
        this.large = new Heap<number>((a, b) => a - b);
    }

    // Helper to "peek" the top: pop then push back
    private top(heap: Heap<number>): number {
        const x = heap.pop()!;
        heap.push(x);
        return x;
    }

    private rebalance(): void {
        // small can have:
        // - same size as large, or
        // - exactly one more element
        if (this.small.size() > this.large.size() + 1) {
            this.large.push(this.small.pop()!);
        } else if (this.small.size() < this.large.size()) {
            this.small.push(this.large.pop()!);
        }
    }

    addNum(num: number): void {
        if (this.small.size() === 0 || num <= this.top(this.small)) {
            this.small.push(num);
        } else {
            this.large.push(num);
        }
        this.rebalance();
    }

    findMedian(): number {
        const total = this.small.size() + this.large.size();
        if (total === 0) return 0; // or throw, depending on what you want

        if (total % 2 === 1) {
            // odd: extra element in small (max-heap)
            return this.top(this.small);
        } else {
            // even: average of max(small) and min(large)
            const leftMax = this.top(this.small);
            const rightMin = this.top(this.large);
            return (leftMax + rightMin) / 2;
        }
    }
}
