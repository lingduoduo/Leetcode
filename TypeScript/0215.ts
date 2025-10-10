function findKthLargest(nums: number[], k: number): number {
    const heap = nums.slice(0, k);
    buildMinHeap(heap);

    //go through rest of the items
    for (let i=k; i< nums.length; i++) {
        if (nums[i] > heap[0])
        {
            heap[0] = nums[i];
            heapify(heap, 0)
        }
    }

    return heap[0]
};

function buildMinHeap(heap: number[]) {
    const l = heap.length;
    //cut in the middle to start building heap
    for (let i = Math.floor(l / 2); i>=0; i--) {
        heapify(heap, i)
    }
}

function heapify(heap: number[], i: number) {
    const l = heap.length;
    let min = i;
    const left = 2 * i + 1;
    const right = 2 * i  + 2;
    if( left < l && heap[left] < heap[min]) {
        min = left;
    }
    if (right < l && heap[right] < heap[min])
        min = right;
        
    if (min !== i) {
        [heap[i], heap[min]] = [heap[min], heap[i]]
        heapify(heap, min)
    }
}