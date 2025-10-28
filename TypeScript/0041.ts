function firstMissingPositive(nums: number[]): number {
    const n = nums.length;

    // Normalize: throw away non-[1..n] values
    for (let i = 0; i < n; i++) {
        if (nums[i] <= 0 || nums[i] > n) nums[i] = n + 1;
    }

    // Mark presence by making index (val-1) negative
    for (let i = 0; i < n; i++) {
        const val = Math.abs(nums[i]);
        if (val >= 1 && val <= n) {
            const idx = val - 1;
            if (nums[idx] > 0) nums[idx] = -nums[idx]; // avoid double work
        }
    }

    // First positive index + 1 is the answer
    for (let i = 0; i < n; i++) {
        if (nums[i] > 0) return i + 1;
    }
    return n + 1;
}

