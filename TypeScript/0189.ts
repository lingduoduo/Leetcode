function rotate(nums: number[], k: number): void {
    const n = nums.length;
    k %= n; // handle cases where k > n

    const res = nums.concat(nums); // duplicate array

    for (let i = 0; i < n; i++) {
        nums[i] = res[i + n - k]; // take shifted window
    }
}
