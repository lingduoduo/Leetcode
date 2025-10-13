function searchRange(nums: number[], target: number): number[] {

    // lower bound: first index i with nums[i] >= t
    function lower(t: number): number {
        let l = 0;
        let r = nums.length; // half-open [l, r)
        while (l < r) {
            const mid = Math.floor(l + (r - l) / 2);
            if (nums[mid] < t) l = mid + 1;
            else r = mid;
        }
        return l;
    }

    const left = lower(target);
    // if target not present, early exit
    if (left === nums.length || nums[left] !== target) return [-1, -1];

    // first index >= target+1, minus 1 gives last index == target
    const right = lower(target + 1) - 1;
    return [left, right];
}