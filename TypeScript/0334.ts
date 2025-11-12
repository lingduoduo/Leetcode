function increasingTriplet(nums: number[]): boolean {
    let first = Infinity;
    let second = Infinity;

    for (const num of nums) {
        if (num <= first) {
            first = num;
        } else if (num <= second) {
            second = num;
        } else {
            return true;
        }
    }
    return false;
};
