function removeElement(nums, val) {
    var slowIndex = 0, fastIndex = 0;
    while (fastIndex < nums.length) {
        if (nums[fastIndex] !== val) {
            nums[slowIndex++] = nums[fastIndex];
        }
        fastIndex++;
    }
    return slowIndex;
}
;
var nums = [3, 2, 2, 3];
var val = 3;
console.log(removeElement(nums, val));
