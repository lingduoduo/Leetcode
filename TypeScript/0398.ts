class Solution {
    private pos: Map<number, number[]> = new Map();
    constructor(nums: number[]) {
        this.pos = new Map();
        for (let i = 0; i < nums.length; i++) {
            if (!this.pos.has(nums[i])) {
                this.pos.set(nums[i], []);
            }
            this.pos.get(nums[i])!.push(i);
        }
    }

    pick(target: number): number {
        return this.pos.get(target)![Math.floor(Math.random() * this.pos.get(target)!.length)];
    }
}
