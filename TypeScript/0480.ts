import { Heap } from "heap-js";

function medianSlidingWindow(nums: number[], k: number): number[] {
    // small: max-heap (lower half)
    const small = new Heap<number>((a, b) => b - a);
    // large: min-heap (upper half)
    const large = new Heap<number>(); // default is min-heap

    const delayed = new Map<number, number>(); // value -> lazy delete count
    let smallSize = 0; // valid elements in small
    let largeSize = 0; // valid elements in large

    function incDelayed(val: number) {
        delayed.set(val, (delayed.get(val) ?? 0) + 1);
    }

    function decDelayed(val: number) {
        const cnt = (delayed.get(val) ?? 0) - 1;
        if (cnt <= 0) delayed.delete(val);
        else delayed.set(val, cnt);
    }

    function prune(heap: Heap<number>) {
        // Remove elements from top of heap that are marked in delayed.
        while (!heap.isEmpty()) {
            const top = heap.peek()!;
            const cnt = delayed.get(top) ?? 0;
            if (cnt === 0) break;
            heap.pop();
            decDelayed(top);
        }
    }

    function rebalance() {
        // Ensure:
        // - smallSize == largeSize, or
        // - smallSize == largeSize + 1 (small has the extra one if k is odd)
        if (smallSize > largeSize + 1) {
            const val = small.pop()!;
            large.push(val);
            smallSize--;
            largeSize++;
            prune(small);
        } else if (smallSize < largeSize) {
            const val = large.pop()!;
            small.push(val);
            largeSize--;
            smallSize++;
            prune(large);
        }
    }

    function add(num: number) {
        if (small.isEmpty() || num <= small.peek()!) {
            small.push(num);
            smallSize++;
        } else {
            large.push(num);
            largeSize++;
        }
        rebalance();
    }

    function remove(num: number) {
        // Lazy-remove a value from the window.
        incDelayed(num);

        if (!small.isEmpty() && num <= small.peek()!) {
            smallSize--;
            if (num === small.peek()!) {
                prune(small);
            }
        } else {
            largeSize--;
            if (!large.isEmpty() && num === large.peek()!) {
                prune(large);
            }
        }

        rebalance();
    }

    function getMedian(): number {
        if (k % 2 === 1) {
            // odd: small has one extra element
            return small.peek()!;
        } else {
            // even: average of max(small) and min(large)
            return (small.peek()! + large.peek()!) / 2;
        }
    }

    // 1) Initialize first window
    for (let i = 0; i < k; i++) {
        add(nums[i]);
    }
    const res: number[] = [getMedian()];

    // 2) Slide the window
    for (let i = k; i < nums.length; i++) {
        add(nums[i]);          // add new element
        remove(nums[i - k]);   // remove outgoing element
        res.push(getMedian());
    }

    return res;
}
