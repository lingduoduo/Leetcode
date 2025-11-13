class Solution {
    private presum: number[];
    private total: number;

    constructor(w: number[]) {
        this.presum = [];
        for (let i = 0; i < w.length; i++) {
            if (i === 0) {
                this.presum.push(w[i]);
            } else {
                this.presum.push(this.presum[i - 1] + w[i]);
            }
        }
        this.total = this.presum[this.presum.length - 1];
    }

    pickIndex(): number {
        let target = this.total * Math.random();
        let left = 0, right = this.presum.length - 1;

        while (left < right) {
            let mid = Math.floor((left + right) / 2);
            if (this.presum[mid] < target) {
                left = mid + 1;
            } else {
                right = mid;
            }
        }

        return left;
    }
}
