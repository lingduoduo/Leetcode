function minSubArrayLen(target: number, nums: number[]): number {
    let left: number = 0,
        res: number = Infinity,
        tot: number = 0;

    for (let right: number = 0; right < nums.length; right++) {
        tot += nums[right];

        while (tot >= target) {
            res = Math.min(res, right - left + 1);
            tot -= nums[left];
            left += 1;
        }
    }
    return res === Infinity ? 0 : res;
}

// ✅ Test cases
console.log(minSubArrayLen(7, [2,3,1,2,4,3]));       // 2 -> [4,3]
console.log(minSubArrayLen(15, [1,2,3,4,5]));        // 5 -> [1,2,3,4,5]
console.log(minSubArrayLen(4, [1,4,4]));             // 1 -> [4]
console.log(minSubArrayLen(11, [1,2,3,4,5]));        // 3 -> [3,4,5] = 12
console.log(minSubArrayLen(100, [1,2,3]));           // 0 -> none
console.log(minSubArrayLen(7, []));                  // 0
console.log(minSubArrayLen(0, [1,2,3]));             // 0
