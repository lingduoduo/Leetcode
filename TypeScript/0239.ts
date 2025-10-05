class Solution{
    maxSlidingWindow(nums: number[], k: number): number[] {
        const queue: number[] = [];
        const res: number[] = [];
        for (let i = 0; i < nums.length; i++) {
            while (queue.length && nums[queue[queue.length - 1]] <= nums[i]) queue.pop();
            queue.push(i);
            if (queue.length && queue[0] <= i - k) queue.shift();
            if (i >= k - 1) res.push(nums[queue[0]]);
        }
        return res
    }
};
