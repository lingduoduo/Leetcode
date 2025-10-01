class Solution {
    intersection(nums1: number[], nums2: number[]): number[] {
        const set1 = new Set(nums1);
        const set2 = new Set(nums2);

        const result: number[] = [];
        for (const num of set1) {
            if (set2.has(num)) {
                result.push(num);
            }
        }
        return result;
    }
}

// Example usage:
const sol = new Solution();
console.log(sol.intersection([1, 2, 2, 1], [2, 2])); // [2]
console.log(sol.intersection([4, 9, 5], [9, 4, 9, 8, 4])); // [4, 9]