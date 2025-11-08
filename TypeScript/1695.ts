function maximumUniqueSubarray(nums: number[]): number {
    let res = 0;
    let currentSum = 0;
    let left = 0;
    const seen = new Set<number>();

    for (let right = 0; right < nums.length; right++) {
        const num = nums[right];

        while (seen.has(num)) {
            seen.delete(nums[left]);
            currentSum -= nums[left];
            left += 1;
        }

        seen.add(num);
        currentSum += num;
        res = Math.max(res, currentSum);
    }

    return res;
}
