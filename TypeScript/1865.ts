class FindSumPairs {
    private nums1: number[];
    private nums2: number[];
    private countMap: Map<number, number>;
    constructor(nums1: number[], nums2: number[]) {
        this.nums1 = nums1;
        this.nums2 = nums2;
        this.countMap = new Map<number, number>();
        for (const num of nums2) {
            this.countMap.set(num, (this.countMap.get(num) || 0) + 1);
        }
    }

    add(index: number, val: number): void {
        const oldVal = this.nums2[index];
        this.countMap.set(oldVal, this.countMap.get(oldVal)! - 1);
        if (this.countMap.get(oldVal) === 0) {
            this.countMap.delete(oldVal);
        }
        this.nums2[index] += val;
        const newVal = this.nums2[index];
        this.countMap.set(newVal, (this.countMap.get(newVal) || 0) + 1);
    }

    count(tot: number): number {
        let result = 0;
        for (const num of this.nums1) {
            const complement = tot - num;
            if (this.countMap.has(complement)) {
                result += this.countMap.get(complement)!;
            }
        }
        return result;
    }
}
