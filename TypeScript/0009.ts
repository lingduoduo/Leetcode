function isPalindrome(x: number): boolean {
    if (x < 0) return false;

    if (x === 0) return true;

    let nums = [];

    while (x > 0){
        nums.push(x % 10);
        x = Math.floor(x / 10);
    }

    let left = 0;
    let right = nums.length - 1;

    while (left < right){
        if (nums[left] !== nums[right]) return false;
        left++;
        right--;
    }
    return true;
};