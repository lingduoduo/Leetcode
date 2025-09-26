class Solution {
    removeElement(nums: number[], val: number): number {
        let i = 0;
        for (let j = 0; j < nums.length; j++) {
            if (nums[j] !== val) {
                nums[i] = nums[j];
                i++;
            }
        }
        return i;
    }
}

// Example usage
const sol = new Solution();
const numbers = [3, 2, 2, 3, 4, 3, 5];
const val = 3;
const newLength = sol.removeElement(numbers, val);

console.log(newLength);                   // 4
console.log(numbers.slice(0, newLength)); // [2, 2, 4, 5]
