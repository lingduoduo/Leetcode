class NumArray {
    private cumsum = [0];
    constructor(nums: number[]) {
        let prev = 0
        for (let i =0; i < nums.length; i++){
            this.cumsum.push(prev + nums[i]);
        }
    }

    sumRange(left: number, right: number): number {
        return this.cumsum[right+1] - this.cumsum[left]
    }
}
