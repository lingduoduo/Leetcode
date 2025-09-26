function removeElement(nums: number[], val: number): number {
    let i = 0;
    for (let j = 0; j < nums.length; j++) {
        if (nums[j] !== val) {
            nums[i] = nums[j];
            i++;
        }
    }
    return i;
}

// Example usage:
const numbers = [3, 2, 2, 3, 4, 3, 5];
const val = 3;
const newLength = removeElement(numbers, val);

console.log(newLength);                  // Output: 4
console.log(numbers.slice(0, newLength)); // Output: [2, 2, 4, 5]
