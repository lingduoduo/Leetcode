class Solution{
    nextGreaterElements(nums: number[]): number[] {
        const stack: number[] = [];
        const res: number[] = new Array(nums.length).fill(-1);
        const n = nums.length;

        for (let i = 0; i < 2 * n; i++) {
            const idx = i % n;
            while (stack.length && nums[stack[stack.length - 1]] < nums[idx]) {
                const top = stack.pop()!;
                res[top] = nums[idx]; // next greater VALUE
            }
            if (i < n) stack.push(idx); // only push indices from first pass
        }
        return res;
    }
}
