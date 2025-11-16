function maxFrequency(nums: number[], k: number, numOperations: number): number {
    nums.sort((a, b) => a - b);
    const n = nums.length;
    if (n === 0) return 0;

    // Pre-count frequencies of each value (used for the initial answer in Case 1)
    const valueFreq: Map<number, number> = new Map();
    for (const num of nums) {
        valueFreq.set(num, (valueFreq.get(num) || 0) + 1);
    }
    let maxFreq = Math.max(...valueFreq.values());

    // ------------------------------------------------------
    // Case 1: The target value is an element already in nums
    // Any value v in the interval [target - k, target + k]
    // can be converted into target (each with one operation)
    // ------------------------------------------------------
    let left = 0;
    const windowFreq: Map<number, number> = new Map(); // frequency of values currently in the window
    let right = 0;

    for (const target of nums) {
        // Expand the right boundary: include all nums[right] <= target + k
        while (right < n && nums[right] <= target + k) {
            windowFreq.set(nums[right], (windowFreq.get(nums[right]) || 0) + 1);
            right++;
        }

        // Shrink the left boundary: remove values < target - k
        while (left < n && nums[left] < target - k) {
            windowFreq.set(nums[left], (windowFreq.get(nums[left]) || 0) - 1);
            left++;
        }

        const totalInRange = right - left;              // number of elements in [target - k, target + k]
        const alreadyTarget = windowFreq.get(target) || 0; // elements already equal to target

        // We can convert at most numOperations additional elements into target
        const curr = Math.min(
            totalInRange,
            alreadyTarget + numOperations
        );

        maxFreq = Math.max(maxFreq, curr);
    }

    // ------------------------------------------------------
    // Case 2: The target value is a "middle value" not in nums
    // If max - min <= 2k within a window, all numbers in the
    // window can be shifted into some middle value v.
    // But converting each element requires one operation,
    // so frequency is limited by numOperations.
    // ------------------------------------------------------
    left = 0;
    for (let right = 0; right < n; right++) {
        // Ensure nums[right] - nums[left] <= 2*k
        while (nums[right] - nums[left] > 2 * k) {
            left++;
        }

        const windowSize = right - left + 1;
        const curr = Math.min(windowSize, numOperations);
        maxFreq = Math.max(maxFreq, curr);
    }

    return maxFreq;
};
