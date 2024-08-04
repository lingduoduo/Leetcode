function search(nums, target) {
    var mid, left = 0, right = nums.length;
    while (left < right) {
        mid = left + ((right - left) >> 1);
        if (nums[mid] > target) {
            right = mid;
        }
        else if (nums[mid] < target) {
            left = mid + 1;
        }
        else {
            return mid;
        }
    }
    return -1;
}
;
var nums = [1, 2, 3, 4, 5, 6];
var target = 3;
var result = search(nums, target);
console.log(result); // 2
